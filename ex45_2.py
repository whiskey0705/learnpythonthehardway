import ex45_1 as g

pom = g.Prince(200, 'pom')
lina = g.Princess('gold', 'lina')
snk = g.Alien(400, 'snk')



game = g.Game(pom, snk, lina)
game.play()
