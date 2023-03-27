# Colab

## Prevent from disconnect

> update: 2023/03/27

```=javascript
function ConnectButton(){
    console.log("Connect pushed"); 
    document.querySelector("#top-toolbar > colab-connect-button").shadowRoot.querySelector("#connect").click() 
}
setInterval(ConnectButton, 60000);
```

Reference
- https://stackoverflow.com/questions/71456390/how-to-keep-the-google-colab-running-without-disconnecting-in-2022