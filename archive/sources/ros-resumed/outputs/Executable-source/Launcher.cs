using System;
using System.Diagnostics;
using System.IO;
using System.IO.Compression;
using System.Reflection;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Windows.Forms;

[assembly: AssemblyTitle("Vacuum Lab")]
[assembly: AssemblyProduct("Vacuum Lab")]
[assembly: AssemblyVersion("2.0.0.0")]

internal static class Launcher
{
    [STAThread]
    private static int Main(string[] args)
    {
        bool check = Array.IndexOf(args, "--check") >= 0;
        string report = null;
        int reportIndex = Array.IndexOf(args, "--report");
        if (reportIndex >= 0 && reportIndex + 1 < args.Length) report = args[reportIndex + 1];
        string home = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "VacuumLab");
        Directory.CreateDirectory(home);
        try
        {
            byte[] payload;
            using (Stream resource = Assembly.GetExecutingAssembly().GetManifestResourceStream("VacuumLab.Payload"))
            using (MemoryStream memory = new MemoryStream())
            {
                resource.CopyTo(memory);
                payload = memory.ToArray();
            }
            string hash;
            using (SHA256 digest = SHA256.Create()) hash = BitConverter.ToString(digest.ComputeHash(payload)).Replace("-", "").ToLowerInvariant();
            string app = Path.Combine(home, "app", hash.Substring(0, 16));
            using (Mutex extraction = new Mutex(false, "Local\\VacuumLabExtraction"))
            {
                bool locked;
                try { locked = extraction.WaitOne(30000); }
                catch (AbandonedMutexException) { locked = true; }
                if (!locked) throw new Exception("Another launcher is preparing the files. Try again shortly.");
                try
                {
                    if (!File.Exists(Path.Combine(app, ".complete")))
                    {
                        Directory.CreateDirectory(Path.GetDirectoryName(app));
                        string stage = app + "-" + Guid.NewGuid().ToString("N");
                        Directory.CreateDirectory(stage);
                        using (MemoryStream memory = new MemoryStream(payload))
                        using (ZipArchive zip = new ZipArchive(memory, ZipArchiveMode.Read))
                        {
                            string prefix = Path.GetFullPath(stage) + Path.DirectorySeparatorChar;
                            foreach (ZipArchiveEntry entry in zip.Entries)
                            {
                                string target = Path.GetFullPath(Path.Combine(stage, entry.FullName));
                                if (!target.StartsWith(prefix, StringComparison.OrdinalIgnoreCase)) throw new Exception("Invalid bundled file path.");
                                if (String.IsNullOrEmpty(entry.Name)) { Directory.CreateDirectory(target); continue; }
                                Directory.CreateDirectory(Path.GetDirectoryName(target));
                                using (Stream input = entry.Open())
                                using (FileStream output = File.Create(target)) input.CopyTo(output);
                            }
                        }
                        File.WriteAllText(Path.Combine(stage, ".complete"), hash);
                        if (Directory.Exists(app)) throw new Exception("Incomplete app folder: " + app);
                        Directory.Move(stage, app);
                    }
                }
                finally { extraction.ReleaseMutex(); }
            }
            string powershell = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.System), "WindowsPowerShell", "v1.0", "powershell.exe");
            string script = Path.Combine(app, "Vacuum-Lab.ps1");
            string mode = check ? " -CheckOnly" : Array.IndexOf(args, "--drive") >= 0 ? " -DriveNow" : Array.IndexOf(args, "--files") >= 0 ? " -Files" : "";
            ProcessStartInfo start = new ProcessStartInfo(powershell, "-NoProfile -STA -File \"" + script + "\"" + mode);
            start.WorkingDirectory = app;
            start.UseShellExecute = false;
            start.CreateNoWindow = true;
            start.RedirectStandardOutput = true;
            start.RedirectStandardError = true;
            using (Process process = Process.Start(start))
            {
                var stdout = process.StandardOutput.ReadToEndAsync();
                var stderr = process.StandardError.ReadToEndAsync();
                process.WaitForExit();
                string message = "App files: " + app + Environment.NewLine + stdout.Result + stderr.Result;
                File.WriteAllText(Path.Combine(home, "launcher.log"), message, Encoding.UTF8);
                if (report != null) File.WriteAllText(report, message, Encoding.UTF8);
                if (process.ExitCode != 0 && !check) MessageBox.Show(message, "Vacuum Lab could not start", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return process.ExitCode;
            }
        }
        catch (Exception error)
        {
            string message = error.ToString();
            File.WriteAllText(Path.Combine(home, "launcher.log"), message);
            if (report != null) File.WriteAllText(report, message);
            if (!check) MessageBox.Show(error.Message, "Vacuum Lab", MessageBoxButtons.OK, MessageBoxIcon.Error);
            return 1;
        }
    }
}
