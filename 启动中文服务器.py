
"""
Eaglercraft 1.12.2 中文版启动服务器
双击运行即可！
"""
import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8888
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def main():
    print("="*60)
    print("    Eaglercraft 1.12.2 中文版服务器")
    print("="*60)
    print()
    print(f"目录: {DIRECTORY}")
    print()
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            url = f"http://localhost:{PORT}/Eaglercraft_IR_1.12.2.html"
            print(f"✅ 服务器已启动！")
            print()
            print(f"请在浏览器打开: {url}")
            print()
            print("提示:")
            print("  - 保持此窗口打开")
            print("  - 按 Ctrl+C 关闭服务器")
            print()
            try:
                webbrowser.open(url)
                print("🌐 正在自动打开浏览器...")
            except Exception:
                pass
            httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("\n👋 正在关闭...")
        sys.exit(0)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"\n❌ 端口 {PORT} 被占用了！")
            print("尝试关闭其他可能占用的程序后重试")
        else:
            print(f"\n❌ 错误: {e}")
        input("\n按回车键退出...")

if __name__ == "__main__":
    main()
