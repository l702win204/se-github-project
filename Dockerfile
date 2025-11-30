# 1. 基础镜像：使用官方轻量级 Python 环境
FROM python:3.9-slim
# 2. 设置容器内的工作目录
WORKDIR /app
# 3. 复制代码：将当前目录下的所有文件复制到容器的 /app 目录
COPY . .
# 4. (可选) 如果有 requirements.txt，可以在这里 pip install
# RUN pip install -r requirements.txt
# 5. 声明端口：告诉使用者这个容器会占用 8080
EXPOSE 8080
# 6. 启动命令：容器启动时执行的 Python 命令
# -u 代表 unbuffered，让日志立即输出，方便调试
CMD ["python", "-u", "api_server.py"]
