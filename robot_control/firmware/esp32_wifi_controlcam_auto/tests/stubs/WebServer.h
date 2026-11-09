#pragma once
#include "WiFi.h"
#include <map>
#include <functional>
#include <stdexcept>

enum HTTPMethod { HTTP_GET, HTTP_POST };
class WebServer {
 public:
  using Arguments = std::map<std::string, std::string>;
  std::map<std::pair<std::string, HTTPMethod>, std::function<void()>> routes;
  Arguments arguments;
  int responseCode = 0;
  std::string responseType, responseBody;
  explicit WebServer(int) {}
  void on(const char* path, HTTPMethod method, std::function<void()> handler) {
    routes[{path, method}] = handler;
  }
  void begin() {}
  void handleClient() {}
  bool hasArg(const char* key) { return arguments.count(key); }
  String arg(const char* key) { return String(arguments[key]); }
  void send(int code, const char* type, const char* body) {
    responseCode = code; responseType = type; responseBody = body;
  }
  void send_P(int code, const char* type, const char* body) { send(code, type, body); }
  void sendHeader(const char*, const char*) {}
  void setContentLength(size_t) {}
  WiFiClient client() { return WiFiClient(); }
  int dispatch(const char* path, HTTPMethod method, const Arguments& args = {}) {
    arguments = args; responseCode = 0; responseBody.clear();
    auto found = routes.find({path, method});
    if (found == routes.end()) throw std::runtime_error("Missing HTTP route");
    found->second();
    return responseCode;
  }
};
