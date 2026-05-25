# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Python.
Built as **Task 3** of the **CodSoft Artificial Intelligence Internship**.

---

## 📌 Features

- 🎬 Movie recommendations based on user preferences
- 🔍 Content-based filtering algorithm
- 📊 Tag matching and similarity scoring
- 🔄 Continuous recommendation loop
- 🎯 Sorted recommendations by relevance
- ❌ Invalid input handling

---

## 🧠 How It Works

```
User selects a movie they like
          ↓
System reads movie tags (genre, type)
          ↓
Compares tags with all other movies
          ↓
Counts matching tags (similarity score)
          ↓
Sorts movies by highest match count
          ↓
Recommends top matching movies!
```

---

## 🎯 Filtering Technique

```
Content-Based Filtering:
→ Each movie has tags (action, romance, scifi etc.)
→ Find movies with most matching tags
→ Higher matches = stronger recommendation
```

---

## 🛠️ Tech Stack

- **Language** — Python 3.11
- **Technique** — Content-Based Filtering
- **Libraries** — None (Pure Python!)

---

## 📁 Project Structure

```
CODSOFT-AI-TASK3/
│
├── recommendation.py    # Main recommendation program
└── README.md            # Project documentation
```

---

## ⚙️ How to Run

### Prerequisites
- Python 3.x installed

### Steps

```bash
# Clone the repository
git clone https://github.com/Thol-444/CODSOFT-AI-TASK3.git

# Go to project folder
cd CODSOFT-AI-TASK3

# Run the program
python recommendation.py
```

---

## 🎮 Sample Output

```
========================================
   🎬 Movie Recommendation System
========================================

Available Movies:
  1. Avengers
  2. Inception
  3. Interstellar
  4. The Notebook
  5. Titanic
  6. Toy Story
  7. Finding Nemo
  8. The Dark Knight
  9. Batman Begins
  10. Iron Man

Options:
  1. Get recommendations
  2. Exit

Choose option (1/2): 1
Enter movie name: Iron Man

🎬 Because you liked Iron Man:
-----------------------------------
1. Avengers
   Genre: action, superhero, adventure
2. The Dark Knight
   Genre: action, superhero, dc
3. Batman Begins
   Genre: action, superhero, dc
```

---

## 🎬 Movie Database

| Movie | Tags |
|-------|------|
| Avengers | action, superhero, marvel |
| Iron Man | action, superhero, marvel |
| Inception | thriller, scifi, mystery |
| Interstellar | scifi, space, thriller |
| The Notebook | romance, drama, love |
| Titanic | romance, drama, tragedy |
| Toy Story | animation, comedy, family |
| Finding Nemo | animation, family, adventure |
| The Dark Knight | action, superhero, dc |
| Batman Begins | action, superhero, dc |

---

## 📚 Concepts Covered

- Content-Based Filtering
- Tag similarity scoring
- Dictionary operations in Python
- Sorting algorithms
- Function design
- User input handling

---

## 👩‍💻 Built By

**Nihaarika Tholu**
B.Tech CSE — Anurag University, Hyderabad
[LinkedIn](https://www.linkedin.com/in/nihaarika-tholu-b9186129b/) | [GitHub](https://github.com/Thol-444)

---

## 📜 Internship

This project was built as **Task 3** of the
**CodSoft Artificial Intelligence Internship**

---

⭐ If you found this helpful, give it a star on GitHub!
