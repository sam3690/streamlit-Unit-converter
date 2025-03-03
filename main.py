import streamlit as st

def main():
    st.title("Simple Unit Converter")
    
   # Category selection
    category = st.selectbox(
        "Select conversion type",
        ["Length", "Weight", "Temperature"]
    )
    
    
    value = st.number_input("Enter value to convert:", value=1.0)
    
    if category == "Length":
        # Length conversion
        option = st.selectbox(
            "Choose conversion",
            ["Meters to Feet", "Feet to Meters", "Kilometers to Miles", "Miles to Kilometers"]
        )
        
        if option == "Meters to Feet":
            result = value * 3.281
            st.success(f"{value} meters = {result:.2f} feet")
        elif option == "Feet to Meters":
            result = value / 3.281
            st.success(f"{value} feet = {result:.2f} meters")
        elif option == "Kilometers to Miles":
            result = value * 0.621
            st.success(f"{value} kilometers = {result:.2f} miles")
        elif option == "Miles to Kilometers":
            result = value / 0.621
            st.success(f"{value} miles = {result:.2f} kilometers")
    
    elif category == "Weight":
        # Weight conversion
        option = st.selectbox(
            "Choose conversion",
            ["Kilograms to Pounds", "Pounds to Kilograms"]
        )
        
        if option == "Kilograms to Pounds":
            result = value * 2.205
            st.success(f"{value} kilograms = {result:.2f} pounds")
        elif option == "Pounds to Kilograms":
            result = value / 2.205
            st.success(f"{value} pounds = {result:.2f} kilograms")
    
    elif category == "Temperature":
        # Temperature conversion
        option = st.selectbox(
            "Choose conversion",
            ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
        )
        
        if option == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
            st.success(f"{value} °C = {result:.2f} °F")
        elif option == "Fahrenheit to Celsius":
            result = (value - 32) * 5/9
            st.success(f"{value} °F = {result:.2f} °C")

if __name__ == "__main__":
    main()