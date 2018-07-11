# Parser Job info. with rabbitmq
### Preparation


# Python code
## urls parser
>main.py<br>
>job_urls.py<br>
>muti_Parser.py<br>
>first_page_factory

## detail parser
>main.py<br>
>pageDetailParserClass.py<br>
>pageDetailParserClass.pyc<br>
>my_interview.py<br>
>TBC<br>

# Docker
>docker pull rabbitmq<br>
>docker run -d --hostname my-rabbit --name some-rabbit rabbitmq:3

# Instantiate Celery and decorate functuin
>from celery import Celery<br>
>app = Celery('<file.name>', broker='amqp://guest:guest@localhost:15672')<br>
>@app.task<br>
>def [function]:<br>
>[something else...]
# Run Celery
# Run Docker Rabbitmq
>docker run -d --hostname my-rabbit --name some-rabbit -p 8080:15672 rabbitmq:3-management<br>
>docker run -it --rm --hostname my-rabbit --name some-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
<br>
>docker run -d --hostname my-rabbit --name some-rabbit -p 8080:15672 rabbitmq:3-management<br>

<IronMQ is a cloud-based message queue service developed by Iron.io.>
<AMQP is an open messaging specification>
<RabbitMQ is the most popular implementation (that I know of) of the AMQP specification.>
<PyAMQP is a Python library that lets Python clients communicate with any implementation of AMQP, including RabbitMQ<>
br

# Run Python code
> # In Get_The_Job_v2.0/ <br>
>cd ./detail_parser <br>
>python3 main.py [fileIn] [fileout] <br>
>ex: python3 main.py data/a/error_1.txt data/try_again.csv <br>
> # Then you could get the result <br>

![](https://raw.githubusercontent.com/tkionshao/Get_The_Job_104_v2.0/master/src/figure1.png)