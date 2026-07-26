# IPL Interactive Dashboard with API Integration

## Project Overview

This project is an interactive Streamlit dashboard built using the Indian Premier League (IPL) dataset. The dashboard enables users to explore IPL match statistics by selecting a season from the sidebar. All charts and the data table update automatically based on the selected season. The project also demonstrates integration with a live external REST API using Python's `requests` library.

---

## Objectives

- Build an interactive dashboard using Streamlit.
- Allow users to filter IPL data by season.
- Display multiple visualizations that respond to user input.
- Show a live filtered data table.
- Integrate a live external REST API.
- Deploy the application using Streamlit Community Cloud.

---

## Dataset

The project uses two cleaned IPL datasets:

- `matches_cleaned.csv`
- `deliveries_cleaned.csv`

These datasets are included in the repository, making the project self-contained.

---

## Dashboard Features

### Interactive Input Widget

- Sidebar `SelectBox`
- Users can select an IPL season.
- All visualizations and the data table update automatically based on the selected season.

### Visualizations

The dashboard contains three interactive charts:

1. **Matches by City**
   - Displays the number of matches played in each city for the selected season.

2. **Winning Teams**
   - Displays the number of matches won by each team during the selected season.

3. **Top 10 Batsmen**
   - Displays the top 10 run scorers for the selected season.

### Live Data Table

A filtered match dataset is displayed using `st.dataframe()`, showing only records from the selected season.

---

## External API Integration

The dashboard integrates a live REST API using the Python `requests` library.

### API Endpoint

https://jsonplaceholder.typicode.com/posts/1

### HTTP Method

GET

### Fields Displayed

The dashboard displays the following fields returned by the API:

- id
- title
- body

### API Explanation

The dashboard sends an HTTP GET request to the JSONPlaceholder API. The API returns a JSON response containing information about a sample post. The application parses the JSON response using `response.json()` and displays selected fields inside the Streamlit dashboard.

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Requests

---

## Project Structure

```
IPL_Dashboard/
│
├── app.py
├── matches_cleaned.csv
├── deliveries_cleaned.csv
├── requirements.txt
├── README.md
```

---

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Requirements

The project requires:

- streamlit
- pandas
- matplotlib
- seaborn
- requests

---

## Deployment

The dashboard is deployed using Streamlit Community Cloud.

**Live Dashboard URL:**

```
https://capstone-part3-7zc9a84uhwwhgfhjaba7hb.streamlit.app/
```

---

## Conclusion

This project demonstrates how Streamlit can be used to build interactive dashboards for data exploration. Users can analyze IPL statistics through dynamic charts and tables while also viewing live information retrieved from an external REST API.
