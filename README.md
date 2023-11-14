# Jump quest
juego de plataforma en el cual inicias en el suelo y luego el personaje comenza a saltar de plataforma en plataforma constantemente sin fin!.

## Caracteristicas
- jugador
- plataformas
- poderes repartidos por el mapa
- enemigos repartidad por el mapa
- puntuacion por alcance

## Functionality
Platform are created and it can be quested be te player. The player found enemies and powerups in the road.

___

## Developmen
### Iteration #1
#### Requirements
- Player
- Platforms

#### Arquitecture
**Player**
1. Functinality
    [x] the player have a left, right and jump movements
    [x] engraving
    [] life player and damage in his life

**Platform**
2. Functinality
    [x] zise block
    [x] no mivement, static
We will have a matrix containing a row of platforms, which will be added each time the user goes up n amount of height on the y-axis. After the player climbs n amount, the last platform will be removed.
___
