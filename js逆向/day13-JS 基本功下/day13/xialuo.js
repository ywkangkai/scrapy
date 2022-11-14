
// JS 导包
axios = require('axios')


//设置请求拦截器
axios.interceptors.request.use(function (config) {
    console.log('请求拦截器 成功')
    config.timeout = 2000; //修改请求config
    config.headers['analysis'] = 'eyUvUSRbVhNbVVIbMlMWUQQWKg'
    return config;
}, function (error) {
    console.log('请求拦截器 失败')
    return Promise.reject(error);
});

//设置响应拦截器
axios.interceptors.response.use(function (response) {
    console.log('响应拦截器 成功')
    console.log('调解密函数进行解密数据')
    //return response;
    return response.data; //修改响应数据
}, function (error) {
    console.log('响应拦截器 失败')
    return Promise.reject(error);
});


//发送请求
axios.get('http://httpbin.org/get')
     .then(res=>console.log(res))





