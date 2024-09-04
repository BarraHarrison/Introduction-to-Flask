# Introduction-to-Flask
This project includes a variety of routes that respond to different URLs.
The routes serve static HTML, dynamic content, and render HTML templates.
It also showcases the use of helper functions to generate content dynamically.

# Features
Basic Routing: Demonstrates simple routes that return static HTML content directly.
Dynamic Routing: Shows how to create routes that take dynamic arguments, such as name, age, and product_id.
Template Rendering: Uses Flask’s render_template() function to render HTML pages from the templates directory.
Helper Functions: Includes helper functions like create_title() to dynamically generate HTML content within a route.

# Example Pages:
/: Introduction page with a simple heading.
/homepage: Renders index.html template.
/hello: Returns a "Hello World" message.
/goodbye: Uses the helper function to generate a custom title.
/about: Renders the about.html template.
/contact: Static contact information.
/services: A simple list of services.
/faq: Renders the faq.html template.
/greet/<name>: Dynamically greets the user by name.
/age/<int:age>: Checks if the user is old enough to vote.
/profile/<username>: Displays a user profile page based on the provided username.
/blog: Displays a static blog post message.
/blog/<int:post_id>: Dynamically displays a blog post by post ID.
/gallery: Renders the gallery.html template.
/shop: Displays a shop welcome message.
/product/<int:product_id>: Shows dynamic product details.
/external: Links to an external website.



