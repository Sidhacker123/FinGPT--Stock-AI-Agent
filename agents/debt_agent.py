
from models.schemas import UserRequest, AIResponse

def calculate_foir(income, monthly_obligations):
    return round((monthly_obligations / income) * 100, 2)

def calculate_dscr(income, total_debt_payment):
    return round(income / total_debt_payment, 2)

async def restructure_debt(user_input: UserRequest) -> AIResponse:
    debts = user_input.debt_details or []
    monthly_obligation = 0
    for d in debts:
        try:
            monthly_obligation += float(d.split(":")[1])
        except:
            continue

    foir = calculate_foir(user_input.income, monthly_obligation)
    dscr = calculate_dscr(user_input.income, monthly_obligation)
    actions = []
    if foir > 50:
        actions.append(f"⚠️ High FOIR detected ({foir}%). Consider consolidating high-interest loans.")
    else:
        actions.append(f"✅ FOIR is healthy at {foir}%.")

    if dscr < 1:
        actions.append(f"⚠️ Low DSCR ({dscr}). You may struggle to service current debt. Consider restructuring.")
    else:
        actions.append(f"✅ DSCR is stable at {dscr}.")

    actions.append("📌 Tip: Check if you qualify for lower-rate balance transfers or EMI holidays.")
    summary = "Debt profile analyzed using FOIR and DSCR metrics."
    return AIResponse(summary=summary, actions=actions, data={"FOIR": foir, "DSCR": dscr})
