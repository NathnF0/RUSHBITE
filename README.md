# 🍔 RushBite – Food Ordering System 🍕🍣

RushBite is a **terminal-based food ordering system** connecting customers with businesses, simulating a real delivery experience. Built in Python with **JSON-based data storage**, interactive menus, and easy-to-manage business functionalities.

---

## 🌟 Features

### 🛒 Customer Mode
- Browse food categories: Burger, Pizza, Japanese, etc.
- View all published businesses with:
  - Name
  - Description
  - Opening hours (Open / Closed status based on current time)
- Select products from the menu and add to cart
- View order summary with **itemized prices and total**

### 🏪 Business Mode
- Create a store with **name & password**
- Secure login to manage your business
- Add or remove products
- Customize your store:
  - Category
  - Description
  - Opening hours
- Publish the store to RushBite so customers can see it
- Interactive menus with **tips & explanations** for each option

---

## ⚙️ Technologies
- Python 3.11+
- JSON for data persistence
- Terminal-based menus for interaction

---

## 📂 Project Structure


SISTEMofORDERS-RUSHBITE-/
│
├─ app.py # Main RushBite code
├─ empresas.json # Store & product data
└─ README.md # Project documentation


---

## 🚀 Getting Started

1.**Clone the repository:**
git clone https://github.com/NathnF0/SISTEMofORDERS-RUSHBITE-.git

2.Navigate to the project folder:
cd SISTEMofORDERS-RUSHBITE-

3.Run the application:
python app.py

4.Follow the interactive instructions and choose between Customer Mode or Business Mode.

📝 Notes

A store must be published to appear in Customer Mode.
Store hours are used to display Open/Closed status.
All business data is saved in empresas.json.

💡 Future Improvements

Search & filter products by category
Add images/icons for stores and products
Build a GUI with Tkinter or PyQt
Customer accounts for saving frequent orders
Multi-store cart system
Product & store rating system

👨‍💻 Author

NathnF
Information Systems student, programming and UX enthusiast.
This is my main project, demonstrating the ability to build full systems with interactive menus and persistent data.
