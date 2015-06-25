from http.server import HTTPServer, BaseHTTPRequestHandler
import psutil, datetime

class MyHTTPHandler(BaseHTTPRequestHandler):
	def do_GET(self):
             self.send_response(200)
             self.end_headers()
             res = ""
             boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
             cpu_util = psutil.cpu_percent(interval=1, percpu=True)
             mem = psutil.virtual_memory()
             res="<table width='40%' border=2><tr bgcolor='#CEF6F5'><td>BOOT TIME</td><td>" + boot_time + "</td></tr>"
             res += "<tr><td>CPU UTILIZATION</td><td><table border=0 width='100%'>"
             i = 1
             for cpu in cpu_util:
                 res += "<tr><td>CPU {}</td><td bgcolor=".format(i)
                 if (cpu < 50) :
                     res += "'#008000'> {}%</td></tr>".format(cpu)
                 else:
                     res += "'#ff0000'> {}%</td></tr>".format(cpu)
                 i = i+1
             res += "</table></td></tr><tr bgcolor='#CEF6F5'><td>AVAILABLE MEMORY</td><td>" + str(mem.available) + "</td></tr>"
             res += "<tr><td>USED MEMORY</td><td>" + str(mem.used) + "</td></tr>"
             res += "<tr ><td bgcolor='#CEF6F5'>USED PERCENTAGE</td><td bgcolor="
             if ( mem.percent < 50) :
                 res += "'#008000'>" + str(mem.percent) + "</td></tr></table></div>"
             else:
                 res += "'#ff0000'>" + str(mem.percent) + "</td></tr></table></div>"
             self.wfile.write(bytes(res, 'utf-8'))
             return

server = HTTPServer(("", 8000), MyHTTPHandler)
server.serve_forever()
