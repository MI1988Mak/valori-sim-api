from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="VALORI Simulations-API")

# --- Generische Simulationsstruktur ---
class GenericParameter(BaseModel):
    beispielwert: float

class GenericPayload(BaseModel):
    sim_id: str
    parameter: GenericParameter

def generate_response(sim_id: str, parameter: GenericParameter):
    ergebnis_text = f"Simulationsergebnis für {sim_id} – Beispielwert: {parameter.beispielwert}"
    return JSONResponse(
        content={
            "entscheidung": ergebnis_text,
            "kennzahlen": {"beispielwert": parameter.beispielwert},
            "eingabe": {"sim_id": sim_id, "parameter": parameter.dict()},
            "reizbar": {
                "auftragsklaerung": f"Dies ist eine strukturierte Simulation für {sim_id}.",
                "beispiel": f"Beispielwert war {parameter.beispielwert}",
                "ergebnis": ergebnis_text,
                "revision": "Anpassung bei neuer Zielstruktur möglich"
            }
        },
        media_type="application/json; charset=utf-8"
    )

# Dynamisch alle sim01 bis sim12 erzeugen
for i in range(1, 13):
    sim_route = f"/v1/run-sim{str(i).zfill(2)}"
    sim_id = f"sim{str(i).zfill(2)}"

    async def sim_func(payload: GenericPayload, sim_id=sim_id):
        return generate_response(sim_id, payload.parameter)

    app.post(sim_route)(sim_func)

# Optionaler zentraler Router
@app.post("/v1/run-simulation")
def run_simulation_router(payload: dict):
    sim_id = payload.get("sim_id")
    if sim_id and sim_id.startswith("sim") and sim_id[3:].isdigit():
        return generate_response(sim_id, GenericPayload(**payload).parameter)
    raise HTTPException(status_code=404, detail=f"Simulation '{sim_id}' nicht gefunden.")
