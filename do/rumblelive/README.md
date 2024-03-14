# rumblelive

API to look at your Rumble channel and always return the latest live embed code. You can use this function as an embed code which never changes and always points to the latest live feed.

## Usage

When deploying to Digital Ocean, set the environmental variable `RUMBLE_URL` to one of the URLs at https://rumble.com/account/livestream-api.

## Embed Code

The embed code below will check your function and replace the `div` with your stream when it is live. To use this embed code, **replace** the **function URL** with the URL to your function.

```html
<div id="stream-frame" style="width: 100%; height: 100%; color: white; background-color: black; display: flex; justify-content: center; align-items: center;">
  <h2>Waiting for Stream to Start</h2>
</div>
<script>
function fetch_status() {
  fetch('https://blah.doserverless.co/api/v1/web/fn-url/myproject/rumblelive?ts=' + Date.now())
    .then(response => response.json())
    .then((data) => {
      if (data.status == 'live') {
        document.querySelector("#stream-frame").innerHTML = data.embed;
      } else{
        setTimeout(fetch_status, 10000);
      }
    })
    .catch(e => alert('Error fetching stream status; refresh page.'));
}
fetch_status();
</script>
```
