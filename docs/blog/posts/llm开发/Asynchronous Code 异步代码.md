Asynchronous code just means that the language 💬 has a way to tell the computer / program 🤖 that at some point in the code, it 🤖 will have to wait for _something else_ to finish somewhere else. Let's say that _something else_ is called "slow-file" 📝.  
异步代码只是意味着语言💬有一种方法告诉计算机/程序🤖，在代码中的某个时刻，它🤖将不得不等待其他事情在其他地方完成。假设还有一个东西叫做“慢文件”📝。

So, during that time, the computer can go and do some other work, while "slow-file" 📝 finishes.  
所以，在那段时间里，计算机可以去做一些其他的工作，当“慢文件”📝努力完成时。

Then the computer / program 🤖 will come back every time it has a chance because it's waiting again, or whenever it 🤖 finished all the work it had at that point. And it 🤖 will see if any of the tasks it was waiting for have already finished, doing whatever it had to do.  
然后，计算机/程序🤖每次有机会都会回来，因为它再次等待，或者每当它🤖完成了当时的所有工作。它会查看它正在等待的任何任务是否已经完成，并执行它必须执行的操作。

Next, it 🤖 takes the first task to finish (let's say, our "slow-file" 📝) and continues whatever it had to do with it.  
接下来，它🤖需要完成第一个任务（比方说，我们的“慢文件”📝）并继续与它有关的任何事情。

That "wait for something else" normally refers to I/O operations that are relatively "slow" (compared to the speed of the processor and the RAM memory), like waiting for:  
“等待其他事情”通常是指相对“慢”的 I/O 操作（与处理器和 RAM 内存的速度相比），例如等待：

- the data from the client to be sent through the network  
    来自客户端的数据通过网络发送
- the data sent by your program to be received by the client through the network  
    您的程序发送的数据，客户端通过网络接收
- the contents of a file in the disk to be read by the system and given to your program  
    磁盘中文件的内容由系统读取并提供给您的程序
- the contents your program gave to the system to be written to disk  
    您的程序提供给系统以写入磁盘的内容
- a remote API operation  
    远程API操作
- a database operation to finish  
    要完成的数据库操作
- a database query to return the results  
    数据库查询返回结果
- etc.  
    ETC。

As the execution time is consumed mostly by waiting for I/O operations, they call them "I/O bound" operations.  
由于执行时间主要消耗在等待 I/O 操作上，因此他们将其称为“I/O 绑定”操作。

It's called "asynchronous" because the computer / program doesn't have to be "synchronized" with the slow task, waiting for the exact moment that the task finishes, while doing nothing, to be able to take the task result and continue the work.  
之所以称为“异步”，是因为计算机/程序不必与慢速任务“同步”，等待任务完成的确切时刻，同时什么都不做，就能够获取任务结果并继续工作。

Instead of that, by being an "asynchronous" system, once finished, the task can wait in line a little bit (some microseconds) for the computer / program to finish whatever it went to do, and then come back to take the results and continue working with them.  
相反，通过成为一个“异步”系统，一旦完成，任务可以稍微等待计算机/程序完成它要做的事情，然后返回获取结果并进行计算。继续与他们合作。

For "synchronous" (contrary to "asynchronous") they commonly also use the term "sequential", because the computer / program follows all the steps in sequence before switching to a different task, even if those steps involve waiting.  
对于“同步”（与“异步”相反）他们通常也使用术语“顺序”，因为计算机/程序在切换到不同任务之前按顺序遵循所有步骤，即使这些步骤涉及等待。