# fastapi-crud
Comparison fastapi crud sync and async

### Testing with `ApacheBench`

- sync

```bash
# ab -k -c 35 -n 100 http://[ip_address]:8001/products/1/
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking [ip_address] (be patient).....done


Server Software:        uvicorn
Server Hostname:        [ip_address]
Server Port:            8001

Document Path:          /products/1/
Document Length:        80 bytes

Concurrency Level:      35
Time taken for tests:   30.783 seconds
Complete requests:      100
Failed requests:        11
   (Connect: 0, Receive: 0, Length: 11, Exceptions: 0)
Non-2xx responses:      11
Keep-Alive requests:    0
Total transferred:      22059 bytes
HTML transferred:       7351 bytes
Requests per second:    3.25 [#/sec] (mean)
Time per request:       10774.077 [ms] (mean)
Time per request:       307.831 [ms] (mean, across all concurrent requests)
Transfer rate:          0.70 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1   13  16.3      6      62
Processing:    24 10729 14333.1    365   30229
Waiting:        9 10713 14324.0    349   30187
Total:         26 10742 14328.7    389   30238

Percentage of the requests served within a certain time (ms)
  50%    389
  66%  30102
  75%  30149
  80%  30171
  90%  30178
  95%  30226
  98%  30229
  99%  30238
 100%  30238 (longest request)
```

- async

```bash
# ab -k -c 35 -n 100 http://[ip_address]:8000/products/2/
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking [ip_address] (be patient).....done


Server Software:        uvicorn
Server Hostname:        [ip_address]
Server Port:            8000

Document Path:          /products/2/
Document Length:        74 bytes

Concurrency Level:      35
Time taken for tests:   0.574 seconds
Complete requests:      100
Failed requests:        0
Keep-Alive requests:    0
Total transferred:      21800 bytes
HTML transferred:       7400 bytes
Requests per second:    174.30 [#/sec] (mean)
Time per request:       200.805 [ms] (mean)
Time per request:       5.737 [ms] (mean, across all concurrent requests)
Transfer rate:          37.11 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1    5   4.3      2      12
Processing:    28  170  70.6    169     400
Waiting:       23  168  70.2    167     396
Total:         31  174  71.7    173     408

Percentage of the requests served within a certain time (ms)
  50%    173
  66%    188
  75%    206
  80%    214
  90%    250
  95%    336
  98%    380
  99%    408
 100%    408 (longest request)
```