grammar SongGrammar;

song: phrase+ EOF;
phrase: (chunk ' '?)+ '\n'?;

chunk: pair | triplet;
pair: EMOJI EMOJI;
triplet: EMOJI EMOJI EMOJI;

EMOJI : [\p{Emoji}];
