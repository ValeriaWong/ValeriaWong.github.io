**文档**： [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com/)

**源码**： [https://github.com/tiangolo/fastapi](https://github.com/tiangolo/fastapi)

利用并行性和多处理（并行运行多个进程）的优势来处理 CPU 密集型工作负载

## 第一步总结[¶](https://fastapi.tiangolo.com/zh/tutorial/first-steps/#_9 "Permanent link")

- 导入 `FastAPI`。
- 创建一个 `app` 实例。
- 编写一个**路径操作装饰器**（如 `@app.get("/")`）。
- 编写一个**路径操作函数**（如上面的 `def root(): ...`）。
- 运行开发服务器（如 `uvicorn main:app --reload`）。



`FastAPI` 是直接从 `Starlette` 继承的类。

你可以通过 `FastAPI` 使用所有的 Starlette 的功能。 

### `Starlette` 是什么?
Starlette是一个轻量级的 ASGI 框架/工具包,用于构建高性能 asyncio 服务。
它具有以下一些主要功能和特点:
- 支持 ASGI(Asynchronous Server Gateway Interface) 协议。这是一个异步的 Python web 服务器标准接口。
- 提供了路由,请求和响应处理,会话管理,静态文件处理等 web 开发的基础功能。
- 基于 Python 异步语法,使用 asyncio 和 uvloop 构建,性能很高。
- 可以作为 web 框架直接使用,也可以作为工具包来辅助其他 ASGI 框架。
FastAPI 框架就是直接从 Starlette 继承而来,添加了一些额外的功能,比如:
- 基于类型的自动验证和序列化系统
- 自动生成交互式 API 文档
- 异常处理和验证错误返回
所以简单来说,Starlette提供了异步 web 应用和服务的基础功能,FastAPI在它的基础上进行了扩展,提供了一些更高级、开发更高效的 web API 的功能。它们是很有有机结合的关系。

### Pydantic 模型


### 当使用 GraphQL 时通常你所有的动作都通过 `post` 一种方法执行。
GraphQL作为一种API查询语言,其所有请求都通过POST方法发送到同一个URL上。这有以下几个好处:

1. 更简单的路由设置。客户端只需要发送请求到一个URL,服务器端也只需要在一个端点处理GraphQL查询。不需要为每个资源设置不同的路由。
2. 避免GET请求 query 参数限制。GraphQL查询可能很复杂,包含许多嵌套字段。如果通过GET请求,会受到URL长度限制。
3. 更好的安全性。important 数据都是通过POST提交,不会像GET请求那样直接暴露在URL中。
4. 请求体可以携带复杂参数。GraphQL查询本身就比较复杂,作为请求体发送更加灵活。
5. 缓存机制更加高效。可以基于整个查询语句生成缓存键,而不仅仅依赖URL端点。
6. 符合Restful API最佳实践。复杂查询类操作建议使用POST提交。

总的来说,GraphQL通过POST到单一端点的方式,简化了客户端和服务器端的接入,也使得其灵活性和安全性得到提高。这是GraphQL设计的一个优秀之处。


### async

You can only use `await` inside of functions created with `async def`.  
您只能在使用 async def 创建的函数内部使用await。

#### TLDR: 
If you are using third party libraries that tell you to call them with `await`, like:  
如果您使用的第三方库告诉您使用等待调用它们，例如：

`results = await some_library()`

Then, declare your _path operation functions_ with `async def` like:  
然后，使用 async def 声明路径操作函数，如下所示：

```python
@app.get('/') 
async def read_results():     
	results = await some_library()     
	return results`


```
---


#### details

#### technical details

##### **[[Asynchronous Code 异步代码]]

**Concurrency** and **parallelism** 并发和并行

###### Concurrency + Parallelism: Web + Machine Learning[¶](https://fastapi.tiangolo.com/async/#concurrency-parallelism-web-machine-learning "Permanent link")

With **FastAPI** you can take the advantage of concurrency that is very common for web development (the same main attraction of NodeJS).  
使用 FastAPI，您可以利用 Web 开发中非常常见的并发性（这也是 NodeJS 的主要吸引力）。

But you can also exploit the benefits of parallelism and multiprocessing (having multiple processes running in parallel) for **CPU bound** workloads like those in Machine Learning systems.  
但是，您还可<font color="#c00000">以利用并行性和多处理（并行运行多个进程）的优势来处理 CPU 密集型工作负载</font>，例如机器学习系统中的工作负载。

That, plus the simple fact that Python is the main language for **Data Science**, Machine Learning and especially Deep Learning, make FastAPI a very good match for Data Science / Machine Learning web APIs and applications (among many others).  
再加上 Python 是数据科学、机器学习，尤其是深度学习的主要语言这一简单事实，使得 FastAPI 非常适合数据科学/机器学习 Web API 和应用程序（以及其他许多应用程序）。

To see how to achieve this parallelism in production see the section about [Deployment](https://fastapi.tiangolo.com/deployment/).  
要了解如何在生产中实现这种并行性，请参阅有关部署的部分

##### - **`async` and `await

Modern versions of Python have a very intuitive way to define asynchronous code. This makes it look just like normal "sequential" code and do the "awaiting" for you at the right moments.  
现代版本的 Python 有一种非常直观的方式来定义异步代码。这使得它看起来就像正常的“顺序”代码，并在正确的时刻为您“等待”。

When there is an operation that will require waiting before giving the results and has support for these new Python features, you can code it like:  
当某个操作需要等待才能给出结果并且支持这些新的 Python 功能时，您可以将其编码为：

`burgers = await get_burgers(2)`

The key here is the `await`. It tells Python that it has to wait ⏸ for `get_burgers(2)` to finish doing its thing 🕙 before storing the results in `burgers`. With that, Python will know that it can go and do something else 🔀 ⏯ in the meanwhile (like receiving another request).  
这里的关键是等待。它告诉 Python 在将结果存储在 Burgers 中之前，必须等待 ⏸ get_burgers(2) 完成其操作 🕙。这样，Python 就会知道它可以同时做其他事情🔀⏯（比如接收另一个请求）。

For `await` to work, it has to be inside a function that supports this asynchronicity. To do that, you just declare it with `async def`:  
为了使await工作，它必须位于支持这种异步性的函数内。为此，您只需使用 async def 声明它：

```python
async def get_burgers(number: int):     
	# Do some asynchronous stuff to create the burgers     
	return burgers`

```

...instead of `def`:  
...而不是 def：❌

```python
# This is not asynchronous 
def get_sequential_burgers(number: int):     
	# Do some sequential stuff to create the burgers     
	return burgers`
```

With `async def`, Python knows that, inside that function, it has to be aware of `await` expressions, and that it can "pause" ⏸ the execution of that function and go do something else 🔀 before coming back.  
使用 async def，Python 知道，在该函数内部，它必须了解 wait 表达式，并且它可以“暂停”⏸ 该函数的执行，并在返回之前执行其他操作 🔀。

When you want to call an `async def` function, you have to "await" it. So, this won't work:  
当你想调用 async def 函数时，<font color="#c00000">你必须“等待”它</font>。所以，这行不通：❌

```python
# This won't work, because get_burgers was defined with: 
async def burgers = get_burgers(2)`

```

---

So, if you are using a library that tells you that you can call it with `await`, you need to create the _path operation functions_ that uses it with `async def`, like in:  
因此，如果您使用的库告诉您可以使用 wait 调用它，则需要创建将其与 async def 一起使用的路径操作函数，如下所示：✅

```python

@app.get('/burgers') 
async def read_burgers():     
	burgers = await get_burgers(2)    
	return burgers`

```


###### More technical details[¶](https://fastapi.tiangolo.com/async/#more-technical-details "Permanent link")

You might have noticed that `await` can only be used inside of functions defined with `async def`.  
您可能已经注意到，await 只能在使用 async def 定义的函数内部使用。

But at the same time, functions defined with `async def` have to be "awaited". So, <font color="#c00000">functions with `async def` can only be called inside of functions defined with `async def` too.  </font>
但与此同时，使用 async def 定义的函数必须“等待”。因此，<font color="#c00000">具有 async def 的函数也只能在使用 async def 定义的函数内部调用</font>。

So, about the egg and the chicken, <font color="#c00000">how do you call the first `async` function</font>?  
那么，先有蛋还是先有鸡，如何调用第一个异步函数呢？

If you are working with **FastAPI** you don't have to worry about that, because that <font color="#c00000">"first" function will be your _path operation function_,</font> and FastAPI will know how to do the right thing.  
如果您正在使用 FastAPI，则不必担心这一点，因为<font color="#c00000">“第一个”函数将是您的路径操作函数，</font>并且 FastAPI 会知道如何做正确的事情。

But if you want to use `async` / `await` without FastAPI, you can do it as well.  
但如果你想在没有 FastAPI 的情况下使用 async/await，你也可以这样做。

###### Write your own async code[¶](https://fastapi.tiangolo.com/async/#write-your-own-async-code "Permanent link")

Starlette (and **FastAPI**) <font color="#c00000">are based on [AnyIO](https://anyio.readthedocs.io/en/stable/)</font>, which makes it compatible with both Python's standard library [asyncio](https://docs.python.org/3/library/asyncio-task.html) and [Trio](https://trio.readthedocs.io/en/stable/).  
Starlette（和 FastAPI）基于 AnyIO，这使得它与 Python 的标准库 asyncio 和 Trio 兼容。

In particular, you can directly use [AnyIO](https://anyio.readthedocs.io/en/stable/) for your advanced concurrency use cases that require more advanced patterns in your own code.  
特别是，您可以直接将 AnyIO 用于您自己的代码中需要更高级模式的高级并发用例。

And even if you were not using FastAPI, you could also write your own async applications with [AnyIO](https://anyio.readthedocs.io/en/stable/) to be highly compatible and get its benefits (e.g. _structured concurrency_).  
即使您没有使用 FastAPI，您也可以使用 AnyIO 编写自己的异步应用程序，以实现高度兼容并获得其好处（例如结构化并发）。

###### Other forms of asynchronous code[¶](https://fastapi.tiangolo.com/async/#other-forms-of-asynchronous-code "Permanent link")

This style of using `async` and `await` is relatively new in the language.  
这种使用 async 和 wait 的风格在该语言中相对较新。

But it makes working with asynchronous code a lot easier.  
但它使得使用异步代码变得更加容易。

This same syntax (or almost identical) was also included recently in modern versions of JavaScript (in Browser and NodeJS).  
最近，现代版本的 JavaScript（浏览器和 NodeJS）中也包含了相同的语法（或几乎相同）。

But before that, handling asynchronous code was quite more complex and difficult.  
但在此之前，处理异步代码相当复杂和困难。

In previous versions of Python, you could have used threads or [Gevent](https://www.gevent.org/). But the code is way more complex to understand, debug, and think about.  
<font color="#c00000">在以前版本的 Python 中，您可以使用线程或 Gevent。但代码的理解、调试和思考要复杂得多。</font>

In previous versions of NodeJS / Browser JavaScript, you would have used "<font color="#c00000">callbacks"</font>. Which leads to [callback hell](http://callbackhell.com/).  
在 NodeJS / 浏览器 JavaScript 的早期版本中，您可能会使用“回调”。这会导致回调地狱。
##### [[coroutines 协程]]
**Coroutine** is just the very fancy term for the thing returned by an `async def` function. Python knows that it is something like a function that it can start and that it will end at some point, but that it might be paused ⏸ internally too, whenever there is an `await` inside of it.  
协程只是一个非常奇特的术语，指的是 async def 函数返回的内容。 Python 知道它就像一个函数，它可以启动并且会在某个时刻结束，但它也可能在内部暂停，只要它内部有一个等待。

But all this functionality of using asynchronous code with `async` and `await` is many times summarized as using "coroutines". It is comparable to the main key feature of Go, the "Goroutines".  
但是使用带有 async 和 await 的异步代码的所有这些功能多次被总结为使用“协程”。它可以与 Go 的主要关键功能“Goroutines”相媲美。






If you are using a third party library that communicates with something (a database, an API, the file system, etc.) and doesn't have support for using `await`, (this is currently the case for most database libraries), then declare your _path operation functions_ as normally, with just `def`, like:  
如果您使用的是与某些内容（数据库、API、文件系统等）通信的第三方库，并且不支持使用等待（目前大多数数据库库都是这种情况），则声明您的路径操作正常运行，只需 def，例如：

```python 
@app.get('/') 
def results(): 
	results = some_library() 
	return results
```

If your application (somehow) doesn't have to communicate with anything else and wait for it to respond, use `async def`.  
如果您的应用程序（以某种方式）不需要与其他任何东西通信并等待它响应，请使用 async def。

If you just don't know, use normal `def`.  
如果您不知道，请使用普通的 def。

---

**Note**: You can mix `def` and `async def` in your _path operation functions_ as much as you need and define each one using the best option for you. FastAPI will do the right thing with them.  
注意：您可以根据需要在路径操作函数中混合使用 def 和 async def，并使用最适合您的选项来定义每一个。 FastAPI 会用它们做正确的事情。

Anyway, in any of the cases above, FastAPI will still work asynchronously and be extremely fast.  
无论如何，在上述任何一种情况下，FastAPI 仍然会异步工作并且速度非常快。

But by following the steps above, it will be able to do some performance optimizations.  
但是按照上面的步骤，就能够做一些性能优化了。



#### very technical details

##### Path operation functions[¶](https://fastapi.tiangolo.com/async/#path-operation-functions "Permanent link")

When you declare a _path operation function_ with normal `def` instead of `async def`, it is run in an external threadpool that is then awaited, instead of being called directly (as it would block the server).  
当您使用普通 def 而不是异步 def 声明路径操作函数时，<font color="#c00000">它会在等待的外部线程池中运行，而不是直接调用（因为它会阻塞服务器）</font>。



> 这里的外部线程池指的是Starlette框架内置管理的一个线程池。
当使用普通的 def 方式声明路径操作函数时,因为它是同步函数,如果直接在请求的主事件循环中调用,会阻塞整个事件循环,从而影响服务器的响应能力。
所以Starlette框架会将其封装成一个任务,投递到内置的线程池中执行,然后通过 asyncio 的方式等待其结果。
这样就将同步函数调度到了额外的线程中执行,避免阻塞主事件循环,也能通过 await 获取其结果。
而异步函数本身就是协程形式,可以直接在主循环中以异步方式运行,没有阻塞问题,所以可以直接调用,无需线程池。
所以简单来说,这里的外部线程池,就是Starlette自带的用于处理同步函数的线程池,它使得同步函数也可以与异步服务器模型兼容运行。不会影响到主事件循环和请求处理流程。


If you are coming from another async framework that does not work in the way described above and you are used to defining trivial compute-only _path operation functions_ with plain `def` for a tiny performance gain (about 100 nanoseconds), please note that in **FastAPI** the effect would be quite opposite. In these cases, it's better to use `async def` unless your _path operation functions_ use code that performs blocking I/O.  
如果您来自另一个不能按上述方式工作的异步框架，并且您习惯于使用普通 def 定义简单的仅计算路径操作函数，以获得微小的性能增益（大约 100 纳秒），请注意，在 FastAPI 中效果会适得其反。在这些情况下，最好使用 async def，除非您的路径操作函数使用执行阻塞 I/O 的代码。

Still, in both situations, chances are that **FastAPI** will [still be faster](https://fastapi.tiangolo.com/#performance) than (or at least comparable to) your previous framework.  
尽管如此，在这两种情况下，FastAPI 仍然可能比（或至少与）您以前的框架更快。




##### Dependencies[¶](https://fastapi.tiangolo.com/async/#dependencies "Permanent link")

The same applies for [dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/). If a dependency is a standard `def` function instead of `async def`, it is run in the external threadpool.  
这同样适用于依赖关系。如果依赖项是标准 def 函数而不是 async def，则它在外部线程池中运行。

##### Sub-dependencies[¶](https://fastapi.tiangolo.com/async/#sub-dependencies "Permanent link")

You can have multiple dependencies and [sub-dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/) requiring each other (as parameters of the function definitions), some of them might be created with `async def` and some with normal `def`. It would still work, and the ones created with <font color="#c00000">normal `def` would be called on an external thread (from the threadpool) instead of being "awaited".  </font>
您可以拥有多个相互需要的依赖项和子依赖项（作为函数定义的参数），其中一些可能是使用 async def 创建的，有些可能是使用普通 def 创建的。它仍然可以工作，并且使用普通 def 创建的线程将在外部线程（从线程池）上调用，而不是“等待”。

##### Other utility functions[¶](https://fastapi.tiangolo.com/async/#other-utility-functions "Permanent link")

Any other utility function that you call directly can be created with normal `def` or `async def` and FastAPI won't affect the way you call it.  
您直接调用的任何其他实用函数都可以使用普通 def 或异步 def 创建，并且 FastAPI 不会影响您调用它的方式。

This is in contrast to the functions that FastAPI calls for you: _path operation functions_ and dependencies.  
这与 FastAPI 为您调用的函数形成对比：路径操作函数和依赖项。

If your utility function is a normal function with `def`, it will be called directly (as you write it in your code), not in a threadpool, if the function is created with `async def` then you should `await` for that function when you call it in your code.  
如果你的实用函数是一个带有 def 的普通函数，它将被直接调用（当你在代码中编写它时），而不是在线程池中，如果该函数是用 async def 创建的，那么你应该在调用它时等待该函数在你的代码中。

---

Again, these are very technical details that would probably be useful if you came searching for them.  
同样，这些都是非常技术性的细节，如果您来寻找它们，它们可能会很有用。

Otherwise, you should be good with the guidelines from the section above: [In a hurry?](https://fastapi.tiangolo.com/async/#in-a-hurry).



### 路径

开发 API 时，「路径」是用来分离「关注点」和「资源」的主要手段。

#### 操作[¶](https://fastapi.tiangolo.com/zh/tutorial/first-steps/#_7 "Permanent link")

这里的「操作」指的是一种 HTTP「方法」。

下列之一：

- `POST`
- `GET`
- `PUT`
- `DELETE`

...以及更少见的几种：

- `OPTIONS`
- `HEAD`
- `PATCH`
- `TRACE`

在 HTTP 协议中，你可以使用以上的其中一种（或多种）「方法」与每个路径进行通信。

---

在开发 API 时，你通常使用特定的 HTTP 方法去执行特定的行为。

通常使用：

- `POST`：创建数据。
- `GET`：读取数据。
- `PUT`：更新数据。
- `DELETE`：删除数据。

因此，在 OpenAPI 中，每一个 HTTP 方法都被称为「操作」。

我们也打算称呼它们为「操作」。


### ### 步骤 5：返回内容[¶](https://fastapi.tiangolo.com/zh/tutorial/first-steps/#5 "Permanent link")

`from fastapi import FastAPI  app = FastAPI()  @app.get("/") async def root():     return {"message": "Hello World"}`

你可以返回一个 `dict`、`list`，像 `str`、`int` 一样的单个值，等等。

你还可以返回 Pydantic 模型（稍后你将了解更多）。

还有许多其他将会自动转换为 JSON 的对象和模型（包括 ORM 对象等）。尝试下使用你最喜欢的一种，它很有可能已经被支持。







## 路径参数