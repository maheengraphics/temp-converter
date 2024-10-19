import streamlit as st

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit app
def main():
    st.title("Temperature Converter")
    
    # Dropdown for selection
    option = st.selectbox("Choose conversion type", 
                          ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))
    
    # Celsius to Fahrenheit conversion
    if option == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius", step=0.1)
        if st.button("Convert"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.success(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
    
    # Fahrenheit to Celsius conversion
    elif option == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit", step=0.1)
        if st.button("Convert"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.success(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C")

if __name__ == "__main__":
    main()
 
