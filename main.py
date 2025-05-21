from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="VALORI Simulations-API")

# 12 Simulationen automatisch generieren
for i in range(1, 13):
    param_class = type(
        f"Sim{i:02}_Parameter",
        (BaseModel,),
        {"beispielwert": (float, 100.0)}
    )

    payload_class = type(
        f"Sim{i:02}_Payload",
        (BaseModel,),
        {
            "sim_id": (str, ...),
            "parameter": (param_class, ...)
        }
    )

    def make_endpoint(sim_id):
        async def endpoint(payload):
            p = payload.parameter
            ergebnis_text = f"Simulationsergebnis für sim{sim_id:02} – Beispielwert: {p.beispielwert}"
            return JSONResponse(
                content={
                    "entscheidung": ergebnis_text,
                    "kennzahlen": {"beispielwert": p.beispielwert},
                    "eingabe": payload.dict(),
                    "reizbar": {
                        "auftragsklaerung": f"Dies ist eine strukturierte Simulation für sim{sim_id:02}.",
                        "beispiel": f"Beispielwert war {p.beispielwert}",
                        "ergebnis": ergebnis_text,
                        "revision": "Anpassung bei neuer Zielstruktur möglich"
                    }
                },
                media_type="application/json; charset=utf-8",
                headers={"Content-Type": "application/json; charset=utf-8"}
            )
        return endpoint

    endpoint = make_endpoint(i)
    endpoint.__name__ = f"run_sim{i:02}"
    app.post(f"/v1/run-sim{i:02}")(endpoint)
