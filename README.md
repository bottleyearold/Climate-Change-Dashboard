https://finaldd2-3.onrender.com/

The process of creating this dashboard initially involved brainstorming an idea. There are lots of topics to choose from so this is a difficult decision. Some key thoughts were what topic will present nicely and has easily accessible data. That’s when I decided to make my project on Climate Change, a topic I’m passionate about and a topic with lots of available data. Next I  brainstormed what kind of people would be viewing my page. This is essential before designing a page to know what the audience is looking for. I was able to design 2 personas that would likely use my dashboard. 

I then got a dataset that I could use for my project. Looking through the internet I found a dataset that spoke about the average mean temperature change which aligned exactly with what I wanted to present in my dashboard. It was a good long piece of data that could be used for multiple graphs. I cleaned the data and brainstormed what kind of features and graphs I wanted on my dashboard. To clean my data I used numpy and pandas. I mostly dropped data and renamed it to make my data more usable. I also used melt to convert my data from from wide format to long format and .datana() to drop null data. I decided to include 4 graphs one being a choropleth graph, line graph, and 2 bar graphs. These best presented my data and each had 1-2 filters. The next step in my process was designing the layout of my website. This feature is essential when creating a website. I used Google Slides to see how the layout would look all together. I was able to see what colors were compatible and what layout looked the most visually appealing. 

After designing my layout it was time to implement it. I started using HTML and CSS. I began to develop the start page that described what my dashboard did and elaborated on Climate Change. I wanted a website with multiple pages so I knew I had to implement bootstrap. I used the bootstrap features to develop a navigation bar with 4 categories. I also added a background image using css to make the front page more visually appealing. These were the first things to meet the eyes of the user: the background image, the title, and the navigation bar. For the rest of the page I kept it simple with some facts about climate changes and a couple paragraphs describing key aspects of climate change. 

Following that I created the initial page called Temperature Change that works with dash and python. I began by making a graph using the data I cleaned. To do this I first created an app.layout using components like flexbox and padding to space all corresponding text, titles, sliders, dropdowns, and graphs. Throughout that I decided what aspects of my slider and drop down I wanted including if I wanted multi select one or if I wanted a placeholder as a default I also melted specific data that was going to be used for each corresponding slider and dropdown. Next began making the call backs for the graph, slider, and dropdown. I also added a callback for the default value in the dropdown, which was the United States. I then filtered the data that was being utilized in the graph and developed the layout where each axis, title, and legend. I also modified the ticks and how they would be presented in the graphs.

A struggle I had was in the UI aspect of things was making the bootstrap navigation bar in dash, it looked a little different than it did using html so I had to tweak it to make it look as similar as possible using padding and flexbox to make it look better. I then implemented some text surrounding the graph and a title. Following that I decided I wanted to make the countdown for the time left to limit global warming to 1.5 degrees Celsius. This involved learning the datetime.now() function in python which was pretty simple. To implement this I subtracted the end date to when it’s too late by the datetime.now()  and the datetime library to get the time remaining I then converted it to years, day, hours, minutes, and seconds. 

After that it was time to add another graph with the dataset I used so I decided to make a choropleth since my data include coordinates to make it. For this I didn’t use plotly.express but plotly.graph_objs I first grab the data and clean it but then I realize that I cleaned specific data that was necessary in the past graph so I decide to just duplicate the data so I can clean it correctly for this graph. I then clean the data and create a slider for the graph. I put the graph and slider in my app.layout so it can be positioned correctly below all the divs. To make the choropleth graph interactive I used .update_layout() and specified the contents and what should be modified in the map. I then went over the page using CSS to create a color scheme that I designed for this page. 

Following this page I decided to create another dash page called Results of Climate Change with a line graph and bar graph. Where I used similar functions when it came to designing the dash for this page including structuring objects using app.layout, cleaning the data, and utilizing callbacks. This page also used flexbox and bootstrap for structure and css components such as coloring and padding for styling. Lastly I created a references page in case users wanted to see other sources for information. This consisted of easy html and flexbox with titles and links. I thought to incorporate this just for the whole project to feel holistic and to include everything for a good dashboard. 

After completing the core components of my dashboard I went and rendered my 2 python pages separately and then rendered my html with those links. I modified all the links so they worked for every page. Following that testing mainly consisted of my looking over and reading my dashboard. 
