---
title: httpClient 由3.1 升级到4.5.4
date: 2018-01-29 12:18:54
tags:
- httpClient
---

# Get 方式变更

1. get 的创建方式

由```new GetMethod()```变为```new HttpGet()```


# Post 方式变更

1. post 的创建方式

由```new PostMethod()```变为```new HttpPost()```

2. setRequestBody 方式变更
使用NameValuePair List 的方式
```
    PostMethod postMethod
    NameValuePair[] nvpArray = nvpList.toArray(new NameValuePair[nvpList.size()]);
    postMethod.setRequestBody(nvpArray);
```
变为
```
    List formparams = new ArrayList();
    formparams.add(new BasicNameValuePair("username", "search"));
    formparams.add(new BasicNameValuePair("password", "123"));
    UrlEncodedFormEntity entityList = new UrlEncodedFormEntity(formparams, Consts.UTF_8);
     method.setEntity(entityList);
```


3. setRequestEntity 变更
```
       String logStr = null;
        StringRequestEntity reqEntity = null;
        try {
            reqEntity = new StringRequestEntity(postBodyStr, "text/plain", "utf-8");
        } catch (UnsupportedEncodingException e) {
            logStr = e.getMessage();
            throw new Exception(logStr);
        }
        postMethod.setRequestEntity(reqEntity);
```
变为
```
    StringEntity entity = new StringEntity(postBodyStr, ContentType.create("text/plain", Consts.UTF_8));
    method.setEntity(entity);
```

# 结果读取变更

## 3.1 的方式

```
        String url = "http://www.baidu.com";
        MultiThreadedHttpConnectionManager mgr = new MultiThreadedHttpConnectionManager();
        HttpClient httpClient = new HttpClient(mgr);
        HttpMethod method = new GetMethod(url);
        String logStr = null;
        InputStream in = null;
        InputStreamReader isReader = null;
        BufferedReader reader = null;
        List<String> contentBuffer = new ArrayList<String>();
        try {
            int statusCode = httpClient.executeMethod(method);
            if (statusCode != HttpStatus.SC_OK) {
                logStr = String.format("Rsp is not ok, status code [%s]", statusCode);
                throw new Exception(logStr);
            }
            in = method.getResponseBodyAsStream();
            isReader = new InputStreamReader(in, "utf8");
            reader = new BufferedReader(isReader);
            String inputLine = null;
            while ((inputLine = reader.readLine()) != null) {
                contentBuffer.add(inputLine);
            }
        } catch (IOException e) {
            throw new Exception("error");
        } catch( Exception e ){
            throw new Exception("error");
        }
        System.out.println(StringUtils.join(contentBuffer, ""));
```

## 4.5.4 的方式
```
    String url = "http://www.baidu.com";
    HttpClient client = HttpClientBuilder.create().build();
    HttpGet getMethod = new HttpGet(url);
    String logStr;
    List<String> contentBuffer = new ArrayList<>();
    InputStream is = null;
    try {
        HttpResponse rsp = client.execute(getMethod);
        int status = rsp.getStatusLine().getStatusCode();
        if(status != HttpStatus.SC_OK){
            logStr = String.format("Rsp is not ok, status code [%s]", status);
            throw new Exception(logStr);
        }
        is = rsp.getEntity().getContent();
        InputStreamReader isReader = new InputStreamReader(is, "utf8");
        BufferedReader reader = new BufferedReader(isReader);
        String inputLine = null;
        while ((inputLine = reader.readLine()) != null) {
            contentBuffer.add(inputLine);
        }
    } catch (IOException e) {
        e.printStackTrace();
    }finally {
        if(is != null){
            is.close();
        }
    }

    System.out.println(StringUtils.join(contentBuffer, ""));

```
# 连接池配置变更

3.1 的方式
```
        MultiThreadedHttpConnectionManager mgr = new MultiThreadedHttpConnectionManager();
        //进行连接检测
        //mgr.getParams().setStaleCheckingEnabled(true);
        mgr.getParams().setDefaultMaxConnectionsPerHost(perHostConnCount);
        mgr.getParams().setMaxTotalConnections(totalConnCount);
        mgr.getParams().setConnectionTimeout(connTimeout);
        mgr.getParams().setSoTimeout(getRltTimeout);
        mgr.getParams().setParameter(HttpMethodParams.RETRY_HANDLER, new DefaultHttpMethodRetryHandler(retryTime,false));
        HttpClient httpClientTmp = new HttpClient(mgr);
//        HttpClientParams httpClientParams = new HttpClientParams();
//        httpClientParams.setConnectionManagerTimeout();
        httpClients_.put(urlType, httpClientTmp);
        return httpClientTmp;
```

4.5.4 的方式
```
    RequestConfig requestConfig = RequestConfig.custom()
            .setConnectionRequestTimeout(connectionRequestTimeout)
            .setConnectTimeout(connTimeout)
            .setSocketTimeout(getRltTimeout)
            .build();
            
        PoolingHttpClientConnectionManager cm = new PoolingHttpClientConnectionManager();
        cm.setMaxTotal(totalConnCount);
        cm.setDefaultMaxPerRoute(perHostConnCount);

        HttpRequestRetryHandler try_h = new DefaultHttpRequestRetryHandler(retryTime,false);

        HttpClientBuilder builder = HttpClients.custom();
        builder.setConnectionManager(cm);
        builder.setRetryHandler(try_h);

        return builder.build();
```        

# 参考
* [HttpClient 官网](http://hc.apache.org/httpcomponents-client-4.5.x/quickstart.html)
* [HttpClient接口对比](https://stackoverflow.com/questions/21574478/what-is-the-difference-between-closeablehttpclient-and-httpclient-in-apache-http)
* [HttpClient 参数配置说明](http://jinnianshilongnian.iteye.com/blog/2089792)