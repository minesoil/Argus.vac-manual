$script:LabIconPath=Join-Path $PSScriptRoot 'Vacuum-Lab.ico'
function Set-LabTheme([Windows.Forms.Control]$control) {
    $background=[Drawing.ColorTranslator]::FromHtml('#0B1220')
    $surface=[Drawing.ColorTranslator]::FromHtml('#162338')
    $text=[Drawing.ColorTranslator]::FromHtml('#EAF1FA')
    $muted=[Drawing.ColorTranslator]::FromHtml('#A1B2CC')
    $control.BackColor=$background; $control.ForeColor=$text
    if ($control -is [Windows.Forms.Form]) {
        $control.Font=New-Object Drawing.Font('Segoe UI',10)
        if (Test-Path -LiteralPath $script:LabIconPath) { $control.Icon=New-Object Drawing.Icon($script:LabIconPath) }
    }
    foreach ($child in $control.Controls) { Set-LabTheme $child }
    if ($control -is [Windows.Forms.Button]) {
        $control.FlatStyle='Flat'; $control.FlatAppearance.BorderSize=0
        $control.BackColor=$surface; $control.ForeColor=$text
        $control.Cursor=[Windows.Forms.Cursors]::Hand
        $control.Font=New-Object Drawing.Font('Segoe UI Semibold',10)
        if ($control.Tag -eq 'primary' -or $control.Text -in @('Drive now','Arm drive')) {
            $control.BackColor=[Drawing.ColorTranslator]::FromHtml('#35DEC4'); $control.ForeColor=$background
        } elseif ($control.Tag -eq 'danger' -or $control.Text -match 'STOP|Stop lab') {
            $control.BackColor=[Drawing.ColorTranslator]::FromHtml('#482636'); $control.ForeColor=[Drawing.ColorTranslator]::FromHtml('#FFAFBE')
        }
        $control.FlatAppearance.MouseOverBackColor=[Drawing.ColorTranslator]::FromHtml('#31506A')
        $control.Add_SizeChanged({ Set-LabRoundedRegion $this })
        Set-LabRoundedRegion $control
    } elseif ($control -is [Windows.Forms.TextBox] -or $control -is [Windows.Forms.ComboBox] -or $control -is [Windows.Forms.NumericUpDown]) {
        $control.BackColor=$surface; $control.ForeColor=$text
        if ($control -is [Windows.Forms.TextBox]) { $control.BorderStyle='FixedSingle' }
        if ($control -is [Windows.Forms.ComboBox]) {
            $control.FlatStyle='Flat'; $control.DrawMode='OwnerDrawFixed'; $control.ItemHeight=24
            $control.Add_DrawItem({
                $shade=[Drawing.ColorTranslator]::FromHtml('#162338')
                if (($_.State -band [Windows.Forms.DrawItemState]::Selected) -ne 0) { $shade=[Drawing.ColorTranslator]::FromHtml('#29445C') }
                $brush=New-Object Drawing.SolidBrush($shade)
                try { $_.Graphics.FillRectangle($brush,$_.Bounds) } finally { $brush.Dispose() }
                $caption=$this.Text
                if ($_.Index -ge 0) {
                    $item=$this.Items[$_.Index]
                    $caption=if ($this.DisplayMember) { [string]$item.($this.DisplayMember) } else { $item.ToString() }
                }
                [Windows.Forms.TextRenderer]::DrawText($_.Graphics,$caption,$this.Font,$_.Bounds,[Drawing.ColorTranslator]::FromHtml('#EAF1FA'),([Windows.Forms.TextFormatFlags]::Left -bor [Windows.Forms.TextFormatFlags]::VerticalCenter))
                $_.DrawFocusRectangle()
            })
        }
    } elseif ($control -is [Windows.Forms.ListView]) {
        $control.BackColor=[Drawing.ColorTranslator]::FromHtml('#111C2E'); $control.ForeColor=$text
        $control.BorderStyle='None'; $control.OwnerDraw=$true
        $control.Add_DrawColumnHeader({
            $brush=New-Object Drawing.SolidBrush([Drawing.ColorTranslator]::FromHtml('#23344E'))
            try { $_.Graphics.FillRectangle($brush,$_.Bounds) } finally { $brush.Dispose() }
            [Windows.Forms.TextRenderer]::DrawText($_.Graphics,$_.Header.Text,$this.Font,$_.Bounds,[Drawing.ColorTranslator]::FromHtml('#BFD0E9'),[Windows.Forms.TextFormatFlags]::Left)
        })
        $control.Add_DrawItem({ $_.DrawDefault=$true })
        $control.Add_DrawSubItem({ $_.DrawDefault=$true })
    } elseif ($control -is [Windows.Forms.Label]) {
        if ($control.Tag -eq 'muted') { $control.ForeColor=$muted }
        if ($control.Tag -eq 'accent') { $control.ForeColor=[Drawing.ColorTranslator]::FromHtml('#35DEC4') }
    }
}

function Set-LabRoundedRegion([Windows.Forms.Control]$control) {
    if ($control.Width -lt 20 -or $control.Height -lt 20) { return }
    $path=New-Object Drawing.Drawing2D.GraphicsPath
    $diameter=16; $right=$control.Width-1; $bottom=$control.Height-1
    $path.AddArc(0,0,$diameter,$diameter,180,90)
    $path.AddArc($right-$diameter,0,$diameter,$diameter,270,90)
    $path.AddArc($right-$diameter,$bottom-$diameter,$diameter,$diameter,0,90)
    $path.AddArc(0,$bottom-$diameter,$diameter,$diameter,90,90); $path.CloseFigure()
    $previous=$control.Region; $control.Region=New-Object Drawing.Region($path)
    if ($previous) { $previous.Dispose() }; $path.Dispose()
}
