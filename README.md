## Overview

Risk premiums typically increase during crises, especially wartime, as uncertainty drives investors to demand higher returns. This project analyzes how risk premiums evolve **before**, **during**, and **after** key conflict-related events involving Iran in June 2025:

- **Israel attacks Iran** — *2025-06-13*  
- **USA attacks Iran** — *2025-06-22*  
- **Ceasefire announced** — *2025-06-24*  

To conduct this analysis, we focus on **natural gas** and **crude oil** futures, as they are highly sensitive to geopolitical developments, particularly in the Middle East—a region critical to global energy supply.

For natural gas, we selected **TTF=F**, and for crude oil, **BZ=F**. Price data was extracted using the `yfinance` library.

---
<img width="2089" height="985" alt="download" src="https://github.com/user-attachments/assets/9be5232f-6942-45f8-975d-002706b1d5f4" />
<img width="2090" height="985" alt="download (1)" src="https://github.com/user-attachments/assets/94024305-294a-43d2-9d90-61fca199b51a" />

---

## Key Findings

### ⚔️**Israel Attack (June 13)**  
Both TTF and BZ=F showed positive risk premiums that increased, peaking after four trading days before declining ahead of the US attack.  
This drop likely reflects how, after the initial fear spike, traders realized the conflict was not escalating further and was unlikely to severely disrupt global energy markets.

**Risk Premium Summary:**  
- **TTF:** +1.61 USD average premium, peak of +5.57 USD on day 4  
- **BZ=F:** +0.92 USD average premium, peak of +6.97 USD on day 3  

---

### ⚔️**US Attack (June 22)**  
For gas, the risk premium turned negative—an unexpected outcome. BZ=F also showed a negative premium.  
This significant underpricing suggests that traders probably believed Iran would not retaliate and would likely agree to a ceasefire, especially given the destruction of its nuclear plants by the bunker buster bomb. 

The market appears to have acted **efficiently** here, in line with the market hypothesis theory, as investors correctly anticipated a quick resolution to the conflict, which did occur shortly after.

**Risk Premium Summary:**  
- **TTF:** -3.75 USD average premium  
- **BZ=F:** -9.69 USD average premium  

---

### 🕊️**Ceasefire (June 24)**  
Both TTF and BZ=F exhibited steadily decreasing risk premiums following the ceasefire announcement.  
This is expected, as investor sentiment improved and geopolitical uncertainty **receded**.

**Risk Premium Summary:**  
- **TTF:** -5.35 USD average premium (further 43% decline)  
- **BZ=F:** -9.69 USD average premium (sustained negative premium)  

---

## Conclusions
The **type and perceived escalation** of conflict significantly influence risk premiums. Initial attacks tend to increase premiums as uncertainty spikes, but escalations can lead to declines when markets efficiently anticipate a resolution and price in the expected outcome early. This highlights the role of market efficiency in rapidly incorporating new information during geopolitical events.

--- 
