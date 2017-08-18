meta:
  id: world_list
  endian: be
seq:
  - id: ignored
    type: u4
  - id: world_count
    type: u2
  - id: worlds
    type: world
    repeat: expr
    repeat-expr: world_count
types:
  world:
    seq:
      - id: id
        type: u2
      - id: mask
        type: s4
      - id: address
        type: strz
        encoding: ASCII
      - id: activity
        type: strz
        encoding: ASCII
      - id: location
        type: u1
      - id: player_count
        type: u2
