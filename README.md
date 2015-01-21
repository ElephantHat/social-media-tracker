# social-media-tracker
### A tool for tracking frequency of social media topics, or anything else.

This tool was designed to allow users to see at a glance what topics/items have not been posted about on social media recently. It can easily be adapted for other uses.
* Deploy to Google App Engine (adjust application name in app.yaml as needed)
* Visiting `<application name>.appspot.com/` allows users to see and click on items being tracked
* Visiting `<application name>.appspot.com/admin` allows administrators to add or delete items to track
* Clicking items on the view page resets tracking counter and turns the item green
  * Items turn yellow if not clicked for 10 days
  * Items turn red if not clicked for 15 days
  * Items turn black if not clicked for 20 days


####Planned Additional Features
* Authentication required for admin page
* Specify site name 
* Add/delete multiple item categories
* Specify threshold for item decay 
* ??? Feature/Pull requests welcome!
