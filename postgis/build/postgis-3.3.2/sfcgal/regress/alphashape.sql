SELECT 'ST_AlphaShape_default',
	ST_AsText(ST_AlphaShape('MultiPoint ((6.3 8.4),(7.6 8.8),(6.8 7.3),(5.3 1.8),(9.1 5),(8.1 7),(8.8 2.9),(2.4 8.2),(3.2 5.1),(3.7 2.3),(2.7 5.4),(8.4 1.9),(7.5 8.7),(4.4 4.2),(7.7 6.7),(9 3),(3.6 6.1),(3.2 6.5),(8.1 4.7),(8.8 5.8),(6.8 7.3),(4.9 9.5),(8.1 6),(8.7 5),(7.8 1.6),(7.9 2.1),(3 2.2),(7.8 4.3),(2.6 8.5),(4.8 3.4),(3.5 3.5),(3.6 4),(3.1 7.9),(8.3 2.9),(2.7 8.4),(5.2 9.8),(7.2 9.5),(8.5 7.1),(7.5 8.4),(7.5 7.7),(8.1 2.9),(7.7 7.3),(4.1 4.2),(8.3 7.2),(2.3 3.6),(8.9 5.3),(2.7 5.7),(5.7 9.7),(2.7 7.7),(3.9 8.8),(6 8.1),(8 7.2),(5.4 3.2),(5.5 2.6),(6.2 2.2),(7 2),(7.6 2.7),(8.4 3.5),(8.7 4.2),(8.2 5.4),(8.3 6.4),(6.9 8.6),(6 9),(5 8.6),(4.3 8),(3.6 7.3),(3.6 6.8),(4 7.5),(2.4 6.7),(2.3 6),(2.6 4.4),(2.8 3.3),(4 3.2),(4.3 1.9),(6.5 1.6),(7.3 1.6),(3.8 4.6),(3.1 5.9),(3.4 8.6),(4.5 9),(6.4 9.7))'));
SELECT 'ST_AlphaShape_hole',
	ST_AsText(ST_AlphaShape('MultiPoint ((6.3 8.4),(7.6 8.8),(6.8 7.3),(5.3 1.8),(9.1 5),(8.1 7),(8.8 2.9),(2.4 8.2),(3.2 5.1),(3.7 2.3),(2.7 5.4),(8.4 1.9),(7.5 8.7),(4.4 4.2),(7.7 6.7),(9 3),(3.6 6.1),(3.2 6.5),(8.1 4.7),(8.8 5.8),(6.8 7.3),(4.9 9.5),(8.1 6),(8.7 5),(7.8 1.6),(7.9 2.1),(3 2.2),(7.8 4.3),(2.6 8.5),(4.8 3.4),(3.5 3.5),(3.6 4),(3.1 7.9),(8.3 2.9),(2.7 8.4),(5.2 9.8),(7.2 9.5),(8.5 7.1),(7.5 8.4),(7.5 7.7),(8.1 2.9),(7.7 7.3),(4.1 4.2),(8.3 7.2),(2.3 3.6),(8.9 5.3),(2.7 5.7),(5.7 9.7),(2.7 7.7),(3.9 8.8),(6 8.1),(8 7.2),(5.4 3.2),(5.5 2.6),(6.2 2.2),(7 2),(7.6 2.7),(8.4 3.5),(8.7 4.2),(8.2 5.4),(8.3 6.4),(6.9 8.6),(6 9),(5 8.6),(4.3 8),(3.6 7.3),(3.6 6.8),(4 7.5),(2.4 6.7),(2.3 6),(2.6 4.4),(2.8 3.3),(4 3.2),(4.3 1.9),(6.5 1.6),(7.3 1.6),(3.8 4.6),(3.1 5.9),(3.4 8.6),(4.5 9),(6.4 9.7))', allow_holes => true));

SELECT 'ST_OptimalAlphaShape_default',
  ST_AsText(ST_OptimalAlphaShape('MultiPoint ((6.3 8.4),(7.6 8.8),(6.8 7.3),(5.3 1.8),(9.1 5),(8.1 7),(8.8 2.9),(2.4 8.2),(3.2 5.1),(3.7 2.3),(2.7 5.4),(8.4 1.9),(7.5 8.7),(4.4 4.2),(7.7 6.7),(9 3),(3.6 6.1),(3.2 6.5),(8.1 4.7),(8.8 5.8),(6.8 7.3),(4.9 9.5),(8.1 6),(8.7 5),(7.8 1.6),(7.9 2.1),(3 2.2),(7.8 4.3),(2.6 8.5),(4.8 3.4),(3.5 3.5),(3.6 4),(3.1 7.9),(8.3 2.9),(2.7 8.4),(5.2 9.8),(7.2 9.5),(8.5 7.1),(7.5 8.4),(7.5 7.7),(8.1 2.9),(7.7 7.3),(4.1 4.2),(8.3 7.2),(2.3 3.6),(8.9 5.3),(2.7 5.7),(5.7 9.7),(2.7 7.7),(3.9 8.8),(6 8.1),(8 7.2),(5.4 3.2),(5.5 2.6),(6.2 2.2),(7 2),(7.6 2.7),(8.4 3.5),(8.7 4.2),(8.2 5.4),(8.3 6.4),(6.9 8.6),(6 9),(5 8.6),(4.3 8),(3.6 7.3),(3.6 6.8),(4 7.5),(2.4 6.7),(2.3 6),(2.6 4.4),(2.8 3.3),(4 3.2),(4.3 1.9),(6.5 1.6),(7.3 1.6),(3.8 4.6),(3.1 5.9),(3.4 8.6),(4.5 9),(6.4 9.7))'));
SELECT 'ST_OptimalAlphaShape_hole',
	ST_AsText(ST_OptimalAlphaShape('MultiPoint ((6.3 8.4),(7.6 8.8),(6.8 7.3),(5.3 1.8),(9.1 5),(8.1 7),(8.8 2.9),(2.4 8.2),(3.2 5.1),(3.7 2.3),(2.7 5.4),(8.4 1.9),(7.5 8.7),(4.4 4.2),(7.7 6.7),(9 3),(3.6 6.1),(3.2 6.5),(8.1 4.7),(8.8 5.8),(6.8 7.3),(4.9 9.5),(8.1 6),(8.7 5),(7.8 1.6),(7.9 2.1),(3 2.2),(7.8 4.3),(2.6 8.5),(4.8 3.4),(3.5 3.5),(3.6 4),(3.1 7.9),(8.3 2.9),(2.7 8.4),(5.2 9.8),(7.2 9.5),(8.5 7.1),(7.5 8.4),(7.5 7.7),(8.1 2.9),(7.7 7.3),(4.1 4.2),(8.3 7.2),(2.3 3.6),(8.9 5.3),(2.7 5.7),(5.7 9.7),(2.7 7.7),(3.9 8.8),(6 8.1),(8 7.2),(5.4 3.2),(5.5 2.6),(6.2 2.2),(7 2),(7.6 2.7),(8.4 3.5),(8.7 4.2),(8.2 5.4),(8.3 6.4),(6.9 8.6),(6 9),(5 8.6),(4.3 8),(3.6 7.3),(3.6 6.8),(4 7.5),(2.4 6.7),(2.3 6),(2.6 4.4),(2.8 3.3),(4 3.2),(4.3 1.9),(6.5 1.6),(7.3 1.6),(3.8 4.6),(3.1 5.9),(3.4 8.6),(4.5 9),(6.4 9.7))', allow_holes => true));
