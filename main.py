from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, create_model
import sys

# UTF-8-Konfiguration für stdout (z. B. in Render oder Docker)
sys.stdout.reconfigure(encoding='utf-8')

app = FastAPI(title="VALORI Simulations-API")

# Dynamisch 12 Simulationen generieren: sim01–sim12
for i in range(1, 13):
    sim_id_str = f"sim{i:02}"

    # Parameter-Modell mit Defaultwert
    SimParameter = create_model(f"{sim_id_str}_Parameter", beispielwert=(float, 100.0))
    SimPayload = create_model(
        f"{sim_id_str}_Payload",
        sim_id=(str, ...),
        parameter=(SimParameter, ...)
    )

    # Endpunktfunktion erzeugen
    def make_endpoint(sim_id_inner):
        async def endpoint(payload: SimPayload):
            p = payload.parameter
            ergebnis_text = f"Simulationsergebnis für sim{sim_id_inner:02} – Beispielwert: {p.beispielwert}"
            return JSONResponse(
                content={
                    "entscheidung": ergebnis_text,
                    "kennzahlen": {"beispielwert": p.beispielwert},
                    "eingabe": payload.dict(),
                    "reizbar": {
                        "auftragsklaerung": f"Dies ist eine strukturierte Simulation für sim{sim_id_inner:02}.",
                        "beispiel": f"Beispielwert war {p.beispielwert}",
                        "ergebnis": ergebnis_text,
                        "revision": "Anpassung bei neuer Zielstruktur möglich"
                    }
                },
                media_type="application/json; charset=utf-8",
                headers={"Content-Type": "application/json; charset=utf-8"}
            )
        return endpoint

    # Endpunkt registrieren
    endpoint = make_endpoint(i)
    endpoint.__name__ = f"run_sim{i:02}"  # notwendig für FastAPI Routing
    app.post(f"/v1/run-sim{str(i).zfill(2)}")(endpoint)
