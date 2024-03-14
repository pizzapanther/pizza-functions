# calcache

Takes an iCal URL and serves the file. This is basically a proxy so that you can use something [fullcalendar.io](https://fullcalendar.io/) with out CORS issues. You can take your Google Calendar and embed it on your website and not look default ugly like the Google Calendar embed.

## Usage

When deploying to Digital Ocean make sure to set the environment variable `ICAL_URL` to the URL of the iCal file you wish to serve.
