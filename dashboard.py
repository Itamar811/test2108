import pandas as pd
import matplotlib.pyplot as plt

def analyze_football_data(file_path):
    """dfdfdfdfdf
    פונקציה שמבצעת ניתוח נתונים בסיסי לסטטיסטיקות כדורגל
    :param file_path: נתיב לקובץ CSV עם נתוני משחקי כדורגל
    :return: None
    """
    # קריאת הקובץ
    df = pd.read_csv(file_path)
    print("gg")
    # הצגת מידע כללי
    print("כמות נתונים:", len(df))
    print("עמודות:", df.columns.tolist())
    print("תצוגה כללית של הנתונים:")
    print(df.head())

    # נניח שיש עמודות: 'Team', 'Goals', 'Assists', 'Yellow_Cards'
    if {'Team', 'Goals', 'Assists', 'Yellow_Cards'}.issubset(df.columns):
        # כמה שערים כל קבוצה כבשה
        goals_by_team = df.groupby('Team')['Goals'].sum()
        print("מספר שערים לכל קבוצה:")
        print(goals_by_team)

        # גרף שערים לכל קבוצה
        goals_by_team.sort_values().plot(kind='bar', figsize=(10,5), color='skyblue')
        plt.title('שערים לפי קבוצה')
        plt.xlabel('קבוצה')
        plt.ylabel('שערים')
        plt.tight_layout()
        plt.show()

        # ממוצע אסיסטים וצבירות כרטיסים צהובים
        print("ממוצע אסיסטים:")
        print(df.groupby('Team')['Assists'].mean())
        print("סה\"כ כרטיסים צהובים:")
        print(df.groupby('Team')['Yellow_Cards'].sum())
    else:
        print("הקובץ לא מכיל את כל העמודות הדרושות: 'Team', 'Goals', 'Assists', 'Yellow_Cards'")

# דוגמה לשימוש:
# analyze_football_data('football_data.csv')

