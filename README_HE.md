# Shavian UI Studio

**נוצר על ידי Shavian Music (@shavianofficial).**

זהו Plugin שנועד להפוך את Claude Code למנהל תהליך UI מסודר, ולא למחולל מסכים אקראי.

הדרך המהירה ביותר להתחיל: `/shavian-ui-studio:vision <הרעיון שלך>` — לוקח רעיון מהראש למסך אמיתי עם כמה שאלות, רפרנסים ומוד בורד.

בכל פרויקט חדש הוא:

1. סורק את הפרויקט הקיים.
2. שואל מעט שאלות חדות ומדויקות, וקורא צילומי מסך וסקיצות שתעלה.
3. מבקש רפרנסים חיוביים ושליליים.
4. מריץ סיעור מוחות במקביל (כמה אייג'נטים) ושומר אותו כמוד בורד — ב-Figma כשמחובר, אחרת כקובץ HTML מקומי.
5. משתמש ב-Mobbin למחקר patterns כאשר החיבור פעיל.
6. משתמש ב-Figma לקריאה ולכתיבה native כאשר החיבור פעיל.
7. יוצר `design-brain/` מקומי לפרויקט.
8. שומר החלטות שאושרו כדי שלא ילך אחורה בכל איטרציה.
9. מפעיל critic נפרד שנותן חוות דעת כנה.
10. משווה UI ממומש ל-golden screenshots.
11. לומד את הטעם שלך לאורך זמן ובין פרויקטים (`~/.claude/shavian-ui-studio/taste-profile.md`).

## עקרונות בטיחות

החבילה לא מפעילה פעולות נסתרות:

- אין hooks אוטומטיים.
- אין MCP שמתווסף אוטומטית.
- אין telemetry.
- אין איסוף סיסמאות או tokens.
- אין העלאת assets לשירות חיצוני ללא אישור.
- אין כתיבה ל-Figma ללא אישור מפורש.
- כל מחקר חיצוני נחשב מידע לא מהימן עד שנבדק.

## בדיקה מקומית

```bash
bash scripts/test-local.sh
```

## התקנה מקומית

```bash
bash scripts/install-local.sh
```

אחר כך פתח Claude Code בתוך הפרויקט והריץ:

```text
/shavian-ui-studio:doctor
/shavian-ui-studio:bootstrap
```

## חיבור Figma ו-Mobbin

קרא את `docs/INTEGRATIONS.md` והריץ:

```bash
bash scripts/configure-integrations.sh
```

הסקריפט מציג כל פקודה לפני ההרצה ומבקש אישור.

## שיתוף עם חברים

לאחר העלאת התיקייה ל-GitHub, החברים שלך יוכלו להריץ:

```text
/plugin marketplace add YOUR_GITHUB_USERNAME/YOUR_REPOSITORY
/plugin install shavian-ui-studio@shavian-tools
```

הפרויקט עצמאי ואינו קשור רשמית ל-Anthropic, Figma או Mobbin.
