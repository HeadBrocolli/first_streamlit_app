import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
#streamlit.text('Omega 3 & Blueberry Oatmeal 🥣')
streamlit.text('Kale, 🥗 Spinach & Rocket Smoothie🍞')
streamlit.text('Hard-Boiled 🐔 Free-Range Egg')
streamlit.text('🥑Avocados Toast')
streamlit.header('Build your own food')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_row)





