# STP Claim Root Bridge Attack - Scapy

## Autor
Nombre: Stephan Cedano
Matrícula: 2024-1404

---

## Video demostrativo

[Ver video demostrativo] (https://youtu.be/XlFxx-4FgPU)

---

## Objetivo
Elaborar un programa en Python usando la librería Scapy que envíe tramas BPDU alteradas con una prioridad muy baja (0), con el objetivo de que el equipo atacante sea elegido como Root Bridge dentro de una red donde el protocolo STP esté activo.

---

## Topología
- Router
- Switch con STP habilitado
- Host atacante (ubuntu server)
- Host víctima  (Switch)

  ---



---

## Funcionamiento
El programa transmite tramas BPDU manipuladas con prioridad 0 cada dos segundos, con la finalidad de que el switch seleccione al equipo atacante como Root Bridge.

---

## Parámetros
- Interfaz: ens3
- Prioridad: 0
- MAC falsa: 01:80:c2:00:00:00

---

## Mitigación
- BPDU Guard
- Root Guard
- PortFast
- Configuración manual de prioridad STP
