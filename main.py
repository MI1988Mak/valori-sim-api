from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import sys

sys.stdout.reconfigure(encoding='utf-8')
app = FastAPI(title="VALORI Simulations-API")


class Sim01_Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim01_Payload(BaseModel):
    sim_id: str
    parameter: Sim01_Parameter

@app.post("/v1/run-sim01")
def run_sim01(payload: Sim01_Payload):
    p = payload.parameter
    ergebnis_text = "Simulationsergebnis für sim01 – Beispielwert: " + str(p.beispielwert)

    return JSONResponse(
        content={
            "entscheidung": ergebnis_text,
            "kennzahlen": {"beispielwert": p.beispielwert},
            "eingabe": payload.dict(),
            "reizbar": {
                "auftragsklaerung": "Dies ist eine strukturierte Simulation für sim01.",
                "beispiel": f"Beispielwert war {p.beispielwert}",
                "ergebnis": ergebnis_text,
                "revision": "Anpassung bei neuer Zielstruktur möglich"
            }
        },
        media_type="application/json; charset=utf-8",
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

class Sim02_Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim02_Payload(BaseModel):
    sim_id: str
    parameter: Sim02_Parameter

@app.post("/v1/run-sim02")
def run_sim02(payload: Sim02_Payload):
    p = payload.parameter
    ergebnis_text = "Simulationsergebnis für sim02 – Beispielwert: " + str(p.beispielwert)

    return JSONResponse(
        content={
            "entscheidung": ergebnis_text,
            "kennzahlen": {"beispielwert": p.beispielwert},
            "eingabe": payload.dict(),
            "reizbar": {
                "auftragsklaerung": "Dies ist eine strukturierte Simulation für sim02.",
                "beispiel": f"Beispielwert war {p.beispielwert}",
                "ergebnis": ergebnis_text,
                "revision": "Anpassung bei neuer Zielstruktur möglich"
            }
        },
        media_type="application/json; charset=utf-8",
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

class Sim03_Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim03_Payload(BaseModel):
    sim_id: str
    parameter: Sim03_Parameter

@app.post("/v1/run-sim03")
def run_sim03(payload: Sim03_Payload):
    p = payload.parameter
    ergebnis_text = "Simulationsergebnis für sim03 – Beispielwert: " + str(p.beispielwert)

    return JSONResponse(
        content={
            "entscheidung": ergebnis_text,
            "kennzahlen": {"beispielwert": p.beispielwert},
            "eingabe": payload.dict(),
            "reizbar": {
                "auftragsklaerung": "Dies ist eine strukturierte Simulation für sim03.",
                "beispiel": f"Beispielwert war {p.beispielwert}",
                "ergebnis": ergebnis_text,
                "revision": "Anpassung bei neuer Zielstruktur möglich"
            }
        },
        media_type="application/json; charset=utf-8",
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

class Sim04_Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim04_Payload(BaseModel):
    sim_id: str
    parameter: Sim04_Parameter

@app.post("/v1/run-sim04")
def run_sim04(payload: Sim04_Payload):
    p = payload.parameter
    ergebnis_text = "Simulationsergebnis für sim04 – Beispielwert: " + str(p.beispielwert)

    return JSONResponse(
        content={
            "entscheidung": ergebnis_text,
            "kennzahlen": {"beispielwert": p.beispielwert},
            "eingabe": payload.dict(),
            "reizbar": {
                "auftragsklaerung": "Dies ist eine strukturierte Simulation für sim04.",
                "beispiel": f"Beispielwert war {p.beispielwert}",
                "ergebnis": ergebnis_text,
                "revision": "Anpassung bei neuer Zielstruktur möglich"
            }
        },
        media_type="application/json; charset=utf-8",
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

class Sim05_Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim05_Payload(BaseModel):
    sim_id: str
    parameter: Sim05_Parameter

@app.post("/v1/run-sim05")
def run_sim05(payload: Sim05_Payload):
    p = payload.parameter
    ergebnis_text = "Simulationsergebnis für sim05 – Beispielwert: " + str(p.beispielwert)

    return JSONResponse(
        content={
            "entscheidung": ergebnis_text,
            "kennzahlen": {"beispielwert": p.beispielwert},
            "eingabe": payload.dict(),
            "reizbar": {
                "auftragsklaerung": "Dies ist eine strukturierte Simulation für sim05.",
                "beispiel": f"Beispielwert war {p.beispielwert}",
                "ergebnis": ergebnis_text,
                "revision": "Anpassung bei neuer Zielstruktur möglich"
            }
        },
        media_type="application/json; charset=utf-8",
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

class Sim06_Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim06_Payload(BaseModel):
    sim_id: str
    parameter: Sim06_Parameter

@app.post("/v1/run-sim06")
def run_sim06(payload: Sim06_Payload):
    p = payload.parameter
    ergebnis_text = "Simulationsergebnis für sim06 – Beispielwert: " + str(p.beispielwert)

    return JSONResponse(
        content={
            "entscheidung": ergebnis_text,
            "kennzahlen": {"beispielwert": p.beispielwert},
            "eingabe": payload.dict(),
            "reizbar": {
                "auftragsklaerung": "Dies ist eine strukturierte Simulation für sim06.",
                "beispiel": f"Beispielwert war {p.beispielwert}",
                "ergebnis": ergebnis_text,
                "revision": "Anpassung bei neuer Zielstruktur möglich"
            }
        },
        media_type="application/json; charset=utf-8",
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

class Sim07_Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim07_Payload(BaseModel):
    sim_id: str
    parameter: Sim07_Parameter

@app.post("/v1/run-sim07")
def run_sim07(payload: Sim07_Payload):
    p = payload.parameter
    ergebnis_text = "Simulationsergebnis für sim07 – Beispielwert: " + str(p.beispielwert)

    return JSONResponse(
        content={
            "entscheidung": ergebnis_text,
            "kennzahlen": {"beispielwert": p.beispielwert},
            "eingabe": payload.dict(),
            "reizbar": {
                "auftragsklaerung": "Dies ist eine strukturierte Simulation für sim07.",
                "beispiel": f"Beispielwert war {p.beispielwert}",
                "ergebnis": ergebnis_text,
                "revision": "Anpassung bei neuer Zielstruktur möglich"
            }
        },
        media_type="application/json; charset=utf-8",
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

class Sim08_Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim08_Payload(BaseModel):
    sim_id: str
    parameter: Sim08_Parameter

@app.post("/v1/run-sim08")
def run_sim08(payload: Sim08_Payload):
    p = payload.parameter
    ergebnis_text = "Simulationsergebnis für sim08 – Beispielwert: " + str(p.beispielwert)

    return JSONResponse(
        content={
            "entscheidung": ergebnis_text,
            "kennzahlen": {"beispielwert": p.beispielwert},
            "eingabe": payload.dict(),
            "reizbar": {
                "auftragsklaerung": "Dies ist eine strukturierte Simulation für sim08.",
                "beispiel": f"Beispielwert war {p.beispielwert}",
                "ergebnis": ergebnis_text,
                "revision": "Anpassung bei neuer Zielstruktur möglich"
            }
        },
        media_type="application/json; charset=utf-8",
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

class Sim09_Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim09_Payload(BaseModel):
    sim_id: str
    parameter: Sim09_Parameter

@app.post("/v1/run-sim09")
def run_sim09(payload: Sim09_Payload):
    p = payload.parameter
    ergebnis_text = "Simulationsergebnis für sim09 – Beispielwert: " + str(p.beispielwert)

    return JSONResponse(
        content={
            "entscheidung": ergebnis_text,
            "kennzahlen": {"beispielwert": p.beispielwert},
            "eingabe": payload.dict(),
            "reizbar": {
                "auftragsklaerung": "Dies ist eine strukturierte Simulation für sim09.",
                "beispiel": f"Beispielwert war {p.beispielwert}",
                "ergebnis": ergebnis_text,
                "revision": "Anpassung bei neuer Zielstruktur möglich"
            }
        },
        media_type="application/json; charset=utf-8",
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

class Sim10_Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim10_Payload(BaseModel):
    sim_id: str
    parameter: Sim10_Parameter

@app.post("/v1/run-sim10")
def run_sim10(payload: Sim10_Payload):
    p = payload.parameter
    ergebnis_text = "Simulationsergebnis für sim10 – Beispielwert: " + str(p.beispielwert)

    return JSONResponse(
        content={
            "entscheidung": ergebnis_text,
            "kennzahlen": {"beispielwert": p.beispielwert},
            "eingabe": payload.dict(),
            "reizbar": {
                "auftragsklaerung": "Dies ist eine strukturierte Simulation für sim10.",
                "beispiel": f"Beispielwert war {p.beispielwert}",
                "ergebnis": ergebnis_text,
                "revision": "Anpassung bei neuer Zielstruktur möglich"
            }
        },
        media_type="application/json; charset=utf-8",
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

class Sim11_Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim11_Payload(BaseModel):
    sim_id: str
    parameter: Sim11_Parameter

@app.post("/v1/run-sim11")
def run_sim11(payload: Sim11_Payload):
    p = payload.parameter
    ergebnis_text = "Simulationsergebnis für sim11 – Beispielwert: " + str(p.beispielwert)

    return JSONResponse(
        content={
            "entscheidung": ergebnis_text,
            "kennzahlen": {"beispielwert": p.beispielwert},
            "eingabe": payload.dict(),
            "reizbar": {
                "auftragsklaerung": "Dies ist eine strukturierte Simulation für sim11.",
                "beispiel": f"Beispielwert war {p.beispielwert}",
                "ergebnis": ergebnis_text,
                "revision": "Anpassung bei neuer Zielstruktur möglich"
            }
        },
        media_type="application/json; charset=utf-8",
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

class Sim12_Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim12_Payload(BaseModel):
    sim_id: str
    parameter: Sim12_Parameter

@app.post("/v1/run-sim12")
def run_sim12(payload: Sim12_Payload):
    p = payload.parameter
    ergebnis_text = "Simulationsergebnis für sim12 – Beispielwert: " + str(p.beispielwert)

    return JSONResponse(
        content={
            "entscheidung": ergebnis_text,
            "kennzahlen": {"beispielwert": p.beispielwert},
            "eingabe": payload.dict(),
            "reizbar": {
                "auftragsklaerung": "Dies ist eine strukturierte Simulation für sim12.",
                "beispiel": f"Beispielwert war {p.beispielwert}",
                "ergebnis": ergebnis_text,
                "revision": "Anpassung bei neuer Zielstruktur möglich"
            }
        },
        media_type="application/json; charset=utf-8",
        headers={"Content-Type": "application/json; charset=utf-8"}
    )
