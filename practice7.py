var jsonData = JSON.parse(responseBody);
pm.test("set value of varibale",function(){
pm.environment.set("responseData",jsonData.rand);
console.log(jsonData.rand)
})