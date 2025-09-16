# 使用官方的 Python 3.10 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 将 requirements.txt 复制到工作目录
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 将所有应用代码复制到工作目录
COPY . .

# 定义容器启动时执行的命令
CMD ["python", "main.py"]
