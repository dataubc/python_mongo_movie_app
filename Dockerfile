FROM python:3.8.3-slim
LABEL maintainer="Mohammed Salama <dataubc@gmail.com>"
WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install jupyter dnspython pymongo
EXPOSE 8899

# Run app.py when the container launches
CMD ["jupyter", "notebook", "--ip='*'", "--port=8899", "--no-browser", "--allow-root"]