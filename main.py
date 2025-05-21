from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import sys

sys.stdout.reconfigure(encoding='utf-8')
app = FastAPI(title="VALORI Simulations-API")

# 12 Simulationen: sim01–sim12
class Sim01Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim01Payload(BaseModel):
    sim_id: str
    parameter: Sim01Parameter

@app.post("/v1/run-sim01")
def run_sim01(payload: Sim01Payload):
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
class Sim02Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim02Payload(BaseModel):
    sim_id: str
    parameter: Sim02Parameter

@app.post("/v1/run-sim02")
def run_sim02(payload: Sim02Payload):
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
class Sim03Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim03Payload(BaseModel):
    sim_id: str
    parameter: Sim03Parameter

@app.post("/v1/run-sim03")
def run_sim03(payload: Sim03Payload):
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
class Sim04Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim04Payload(BaseModel):
    sim_id: str
    parameter: Sim04Parameter

@app.post("/v1/run-sim04")
def run_sim04(payload: Sim04Payload):
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
class Sim05Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim05Payload(BaseModel):
    sim_id: str
    parameter: Sim05Parameter

@app.post("/v1/run-sim05")
def run_sim05(payload: Sim05Payload):
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
class Sim06Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim06Payload(BaseModel):
    sim_id: str
    parameter: Sim06Parameter

@app.post("/v1/run-sim06")
def run_sim06(payload: Sim06Payload):
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
class Sim07Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim07Payload(BaseModel):
    sim_id: str
    parameter: Sim07Parameter

@app.post("/v1/run-sim07")
def run_sim07(payload: Sim07Payload):
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
class Sim08Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim08Payload(BaseModel):
    sim_id: str
    parameter: Sim08Parameter

@app.post("/v1/run-sim08")
def run_sim08(payload: Sim08Payload):
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
class Sim09Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim09Payload(BaseModel):
    sim_id: str
    parameter: Sim09Parameter

@app.post("/v1/run-sim09")
def run_sim09(payload: Sim09Payload):
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
class Sim10Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim10Payload(BaseModel):
    sim_id: str
    parameter: Sim10Parameter

@app.post("/v1/run-sim10")
def run_sim10(payload: Sim10Payload):
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
class Sim11Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim11Payload(BaseModel):
    sim_id: str
    parameter: Sim11Parameter

@app.post("/v1/run-sim11")
def run_sim11(payload: Sim11Payload):
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
class Sim12Parameter(BaseModel):
    beispielwert: float = 100.0

class Sim12Payload(BaseModel):
    sim_id: str
    parameter: Sim12Parameter

@app.post("/v1/run-sim12")
def run_sim12(payload: Sim12Payload):
    p = payload.parameter
    ergebnis_text = "Simulationsergebnis für sim12 – Beispielwert: " + str(p.beispielwert)

    return JSONResponse(
        content={
