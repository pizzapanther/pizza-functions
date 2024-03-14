# youtubelive

## Usage

When deploying to Digital Ocean, set the environmental variable `OAUTH_TOKEN` and `OAUTH_SECRET` for your Google account.

## Embed Code

The embed code below will check your function and replace the `div` with your stream when it is live. To use this embed code, **replace** the **function URL** with the URL to your function and the **channel ID** with your Youtube channel.

```html
<div id="stream-frame" style="width: 100%; height: 100%; color: white; background-color: black; display: flex; justify-content: center; align-items: center;">
  <h2>Waiting for Stream to Start</h2>
</div>
<script>
function fetch_status() {
  fetch('https://blah.doserverless.co/api/v1/web/fn-blah/myproject/embedcheck?channel=MYCHANNELID&ts=' + Date.now())
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
