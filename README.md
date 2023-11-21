# Jump quest
Platform game in which you start on the ground, and then the character begins to jump from platform to platform endlessly!

## Features
- Player
- Platforms
- Power-ups scattered throughout the map
- Enemies distributed across the map
- Score based on distance

## Functionality
Platforms are created and can be traversed by the player. The player encounters enemies and power-ups along the way.
___

## Developmen
- **Arquitecture:** Clean arquitecture
- **Development Methodology:** Iterative and incremental development

### Iteration #1
**Requirements**
- Player
- Platforms

**Player Functinality**
    [x] the player have a left, right and jump movements
    [x] engraving
    [x] life player and damage in his life

**Platform Functinality**
    [x] zise block
    [x] no mivement, static
We will have a matrix containing a row of platforms, which will be added each time the user goes up n amount of height on the y-axis. After the player climbs n amount, the last platform will be removed.
___
### Iteration #2
Generate rows (layered generation) of platforms. After the player moves beyond the camera's field of view, the rows (level streaming) that are no longer visible are removed, and new rows of platforms are generated.
**Requirements**
- Platforms

**Platform Functinality**
    [] Implement Layered Generation
    [] Implement Level Streaming
___
