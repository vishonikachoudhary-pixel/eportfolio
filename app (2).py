"""
E-Portfolio · Human Capital Management – AS3 · Meridian Forward
Vishonika | Roll No. 26PGDM093

Run locally:   pip install -r requirements.txt
               streamlit run app.py
All figures come from the "Meridian Engineering & AI ₹100 Cr Model" workbook
(₹ crore, model assumptions, not actual results).
"""

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Meridian Forward · AS3 E-Portfolio", page_icon="📘", layout="wide")

YEARS = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]

# ---------------------------------------------------------------------------
# Data taken from the Excel model (₹ Cr)
# ---------------------------------------------------------------------------
revenue = pd.DataFrame(
    {
        "Engineering services": [31.74, 59.80, 80.50, 86.25, 92.00],
        "AI subscriptions": [8.00, 24.00, 44.00, 68.00, 92.00],
        "Onboarding fees": [2.00, 4.00, 5.00, 6.00, 6.00],
    },
    index=YEARS,
)
revenue["Total revenue"] = revenue.sum(axis=1)

pnl = pd.DataFrame(
    {
        "Revenue": [41.74, 87.80, 129.50, 160.25, 190.00],
        "Gross profit": [37.24, 80.60, 119.15, 146.15, 172.30],
        "EBITDA": [-12.40, 3.21, 19.30, 42.55, 62.50],
        "EBIT": [-25.07, -10.05, 5.44, 34.75, 54.10],
        "Net income": [-25.07, -10.05, 5.44, 33.48, 40.58],
    },
    index=YEARS,
)

cash = pd.DataFrame(
    {
        "Free cash flow": [-67.74, -7.09, 9.82, 33.34, 41.38],
        "Cumulative free cash flow": [-67.74, -74.83, -65.00, -31.67, 9.72],
        "Closing cash balance": [32.26, 25.17, 35.00, 68.33, 109.72],
    },
    index=YEARS,
)

people = pd.DataFrame(
    {
        "Engineers (avg FTE)": [115, 200, 250, 250, 250],
        "AI specialists (FTE)": [20, 25, 30, 30, 30],
        "Subscription customers": [10, 30, 55, 85, 115],
    },
    index=YEARS,
)

uses = pd.DataFrame(
    {
        "Use of the ₹100 Cr": [
            "AI platform, servers, workstations (PP&E)",
            "AI models & product software (intangible)",
            "Operating losses & working capital",
            "Contingency (unused buffer)",
        ],
        "₹ Cr": [30.00, 20.00, 24.83, 25.17],
    }
)

# ---------------------------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------------------------
st.sidebar.title("📘 E-Portfolio")
st.sidebar.markdown("**Vishonika**  \nRoll No. 26PGDM093  \nHuman Capital Management – AS3")
page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "1 · Business context",
        "2 · Judgement & decision",
        "3 · Sustain the workforce",
        "4 · The ₹100 Cr model",
        "5 · Key takeaways",
    ],
)
st.sidebar.caption("Figures: Engineering & AI revenue model (₹ Cr). Model assumptions, not actual revenue.")

# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
if page == "🏠 Home":
    st.title("Meridian Forward")
    st.subheader("Human Capital Management – AS3 · E-Portfolio")
    st.markdown("**Vishonika** | Roll No. 26PGDM093")
    st.divider()
    st.markdown(
        """
Meridian's India centre is moving **from service delivery to product ownership**: it must keep
existing customers well served while building engineering capability and recurring AI revenue.

This e-portfolio explains my AS3 presentation, slide by slide, and uses the
**₹100 Cr Engineering & AI expansion model** to show the numbers behind each point.
"""
    )
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Funding", "₹100 Cr")
    c2.metric("Revenue Y1 → Y5", "₹42 → ₹190 Cr")
    c3.metric("Peak cash used", "₹74.8 Cr")
    c4.metric("NPV @ 12% (with TV)", "₹254 Cr")
    st.info("Use the menu on the left to move through the sections.")

elif page == "1 · Business context":
    st.title("1 · From service delivery to product ownership")
    st.caption("Slide 2 · Business context")

    st.header("Business engine: three revenue streams")
    st.markdown(
        """
- **Engineering services**: the India team builds products for Meridian's global units and bills at cost + 15% mark-up.
- **AI maintenance subscriptions**: customers pay ₹80 L a year for an AI product that reads maintenance history and flags problems early.
- **Onboarding fees**: each new customer pays ₹20 L once to clean and connect its data.
"""
    )
    st.bar_chart(revenue[["Engineering services", "AI subscriptions", "Onboarding fees"]])
    st.dataframe(revenue.style.format("₹{:.2f} Cr"), use_container_width=True)
    st.success(
        "AI subscriptions grow from ₹8 Cr to ₹92 Cr, matching engineering by Year 5. "
        "The business shifts from billing hours to owning a product."
    )

    st.header("Capacity reality: headcount ≠ capacity")
    c1, c2, c3 = st.columns(3)
    c1.metric("Existing employees", "60")
    c2.metric("Potential FTE", "15.5")
    c3.metric("Hours potentially free", "1,984 h")
    st.markdown(
        "7,680 productive hours − 5,696 hours of legacy commitments = **1,984 hours** potentially available. "
        "Releasing them still needs **manager approval**."
    )
    hours = pd.DataFrame({"Hours": [5696, 1984]}, index=["Legacy commitments", "Potentially available"])
    st.bar_chart(hours)

    st.header("ELC journey: readiness, not just hiring")
    c1, c2, c3 = st.columns(3)
    c1.metric("Proposed", "4")
    c2.metric("Partial", "1")
    c3.metric("To develop", "5")
    st.markdown(
        "AS2 already addressed **role design, attraction & sourcing, screening & selection, onboarding readiness**. "
        "*Proposed ≠ completed or evidenced.*"
    )
    st.markdown("**Link to the model:** engineers in seat grow from 115 to 250 and AI specialists from 20 to 30.")
    st.line_chart(people[["Engineers (avg FTE)", "AI specialists (FTE)"]])

elif page == "2 · Judgement & decision":
    st.title("2 · The cheapest option was not the safest decision")
    st.caption("Slide 3 · Judgement and decision")
    st.markdown("The revised plan reflects the authority Meridian has **today**, not the authority it may receive later.")

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Earlier option: bounded delegation")
        st.metric("Cost", "₹3.76 L", "3 vendors", delta_color="off")
        st.markdown(
            "Looked attractive: lower vendor cost and below the ₹6 L cap. "
            "But it depended on an architecture threshold that had **not been accepted**."
        )
        st.error("Risk: the plan relied on unapproved delegation.")
    with c2:
        st.subheader("Revised base: retain approvals + one output")
        st.metric("Cost", "₹4.64 L", "4 vendors", delta_color="off")
        st.markdown(
            "The board had not transferred decision rights to India. This plan avoids unapproved delegation "
            "and removes **240 hours** of duplicate customer-pack work once one owner is named."
        )
        st.success("Trade-off: ₹0.88 L more for a workable approval path.")

    options = pd.DataFrame({"Cost (₹ L)": [3.76, 4.64, 6.00]}, index=["Earlier option", "Revised base", "Budget cap"])
    st.bar_chart(options)

    st.header("Next actions")
    actions = pd.DataFrame(
        {
            "When": ["Day 0", "Week 0", "48 hours", "Week 1", "Ready gate"],
            "Action": [
                "Rao names the output owner",
                "Confirm legacy cover + vendors",
                "Provide access",
                "Supervised induction",
                "Live work sample",
            ],
        }
    )
    st.table(actions)

    st.header("Why this matters for the ₹100 Cr")
    st.markdown(
        "The model already keeps a **₹25.17 Cr contingency** for slower sales, slower vendors or "
        "**delayed decision rights**. Choosing the approval-safe plan protects the schedule that the "
        "revenue depends on: Year 1 engineering billing (₹31.7 Cr) assumes hires join after the 8-week lead."
    )
    st.caption("Evidence: AS2 Deliverable 2 · Q5.04–Q5.08 · Q6.02 · P028 and P044. Actions subject to owner acceptance.")

elif page == "3 · Sustain the workforce":
    st.title("3 · The employee journey continues after onboarding")
    st.caption("Slide 4 · Sustain the workforce")
    st.markdown("Next challenge: turn readiness into **reliable performance, capability growth and customer-knowledge continuity**.")

    st.header("One connected employee lifecycle")
    cols = st.columns(5)
    for col, stage in zip(cols, ["READY", "PERFORM", "DEVELOP", "RECOGNISE", "RETAIN / MOVE"]):
        col.info(f"**{stage}**")

    st.header("Proposed role-level measures")
    measures = pd.DataFrame(
        {
            "Role": ["Data-prep specialist", "QA validator", "Legacy knowledge steward", "Engineering / AI"],
            "Proposed measures": [
                "First-pass pack acceptance; onboarding turnaround",
                "Defects caught before release; defect escape rate",
                "Teach-back pass rate; legacy service protection",
                "Delivery quality; product reliability",
            ],
        }
    )
    st.table(measures)
    st.caption("These are proposed measures, not achieved KPI results.")

    st.header("Ownership + knowledge continuity")
    st.markdown(
        """
- **Performance:** line managers review KRAs and KPIs monthly.
- **Development:** role leads and L&D close evidenced KSAB gaps.
- **Rewards & wellbeing:** recognise quality; monitor workload and employee voice.
- **Movement / exit:** managers document handover; HR supports fair processes.
"""
    )

    st.header("Link to the model")
    st.markdown(
        "People are the biggest cost. Personnel spend rises from **₹35.6 Cr to ₹96.2 Cr**, and the model sets aside "
        "**₹2 L per engineer per year** for AI upskilling. Keeping trained people (retention) protects this investment."
    )
    personnel = pd.DataFrame({"Personnel cost (₹ Cr)": [35.60, 62.75, 83.80, 90.00, 96.20]}, index=YEARS)
    st.bar_chart(personnel)
    st.caption("AS4: connect the lifecycle with clear owners and review dates (proposed direction).")

elif page == "4 · The ₹100 Cr model":
    st.title("4 · Is the ₹100 Cr justified?")
    st.caption("Engineering & AI expansion model · ₹ crore")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Peak cash used", "₹74.83 Cr")
    c2.metric("Safety cushion", "₹25.17 Cr")
    c3.metric("Year 5 EBITDA margin", "33%")
    c4.metric("Cash back to ₹100 Cr", "Year 5")

    tab1, tab2, tab3, tab4 = st.tabs(["Profit & loss", "Cash flow", "Use of funds", "Key assumptions"])
    with tab1:
        st.line_chart(pnl[["Revenue", "EBITDA", "Net income"]])
        st.dataframe(pnl.style.format("{:.2f}"), use_container_width=True)
        st.markdown("Losses in Years 1–2 while engineers are hired and customers build up; profitable from **Year 3**.")
    with tab2:
        st.line_chart(cash)
        st.dataframe(cash.style.format("{:.2f}"), use_container_width=True)
        st.markdown(
            "Cash dips to **₹25.17 Cr** in Year 2 but never runs out. Cumulative free cash flow turns positive in **Year 5**."
        )
    with tab3:
        st.bar_chart(uses.set_index("Use of the ₹100 Cr"))
        st.table(uses)
    with tab4:
        st.markdown(
            """
| Driver | Value |
|---|---|
| Loaded cost per engineer | ₹24 L (Year 1), +8% a year |
| Loaded cost per AI specialist | ₹40 L (Year 1), +8% a year |
| Mark-up on engineering services | 15% |
| Subscription fee | ₹80 L per customer per year (flat) |
| Onboarding fee | ₹20 L per new customer |
| Capex in Year 1 | ₹30 Cr PP&E + ₹20 Cr AI models |
| Tax / discount rate / long-term growth | 25% / 12% / 3% |
"""
        )
        st.caption("AI productivity gains on legacy services and price rises are left out to stay conservative.")

    st.header("Verdict")
    c1, c2 = st.columns(2)
    c1.metric("NPV @ 12% (Years 1–5 + terminal value)", "₹254.25 Cr")
    c2.metric("NPV @ 12% (Years 1–5 only)", "−₹14.47 Cr")
    st.success("**Justified:** positive NPV and cash never runs out.")
    st.warning(
        "Stress test: if subscriptions grow half as fast, peak cash used rises to ₹97.9 Cr (only ₹2.1 Cr left) "
        "and NPV falls to ₹28 Cr. The plan only works if customer growth and hiring stay on track, "
        "which is exactly why the HR decisions in sections 2 and 3 matter."
    )

elif page == "5 · Key takeaways":
    st.title("5 · Key takeaways")
    st.markdown(
        """
1. **Headcount is not capacity.** 60 people give only about 15.5 FTE of free time, and releasing it needs approval.
2. **Safe beats cheap.** The ₹4.64 L plan costs ₹0.88 L more but works within the authority Meridian actually has.
3. **Onboarding is the start, not the end.** Perform → develop → recognise → retain keeps capability and customer knowledge.
4. **The numbers back the people plan.** ₹100 Cr covers ₹74.83 Cr peak cash need with a ₹25.17 Cr buffer, but only if hiring and customer growth stay on track.
"""
    )
    st.divider()
    st.subheader("What I learned")
    st.markdown(
        "Linking HR choices to a financial model showed me that people decisions (who owns an output, how fast "
        "hires become productive, who stays) directly drive revenue and cash. A plan has to fit today's "
        "decision rights to be realistic."
    )
    st.caption("Sources: AS3 instructions · AS2 presentation · Engineering & AI revenue model.")
