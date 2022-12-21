// Generated from /home/phalyce/dev/python/emoji/grammar/SongGrammar.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SongGrammarLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, EMOJI=3;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "EMOJI"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "' '", "'\n'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "EMOJI"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public SongGrammarLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "SongGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5\17\b\1\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\3\2\3\2\3\3\3\3\3\4\3\4\2\2\5\3\3\5\4\7\5\3\2\2\3\u0093"+
		"\2%\2%\2,\2,\2\62\2;\2\u00ab\2\u00ab\2\u00b0\2\u00b0\2\u203e\2\u203e\2"+
		"\u204b\2\u204b\2\u2124\2\u2124\2\u213b\2\u213b\2\u2196\2\u219b\2\u21ab"+
		"\2\u21ac\2\u231c\2\u231d\2\u232a\2\u232a\2\u23d1\2\u23d1\2\u23eb\2\u23f5"+
		"\2\u23fa\2\u23fc\2\u24c4\2\u24c4\2\u25ac\2\u25ad\2\u25b8\2\u25b8\2\u25c2"+
		"\2\u25c2\2\u25fd\2\u2600\2\u2602\2\u2606\2\u2610\2\u2610\2\u2613\2\u2613"+
		"\2\u2616\2\u2617\2\u261a\2\u261a\2\u261f\2\u261f\2\u2622\2\u2622\2\u2624"+
		"\2\u2625\2\u2628\2\u2628\2\u262c\2\u262c\2\u2630\2\u2631\2\u263a\2\u263c"+
		"\2\u2642\2\u2642\2\u2644\2\u2644\2\u264a\2\u2655\2\u2662\2\u2662\2\u2665"+
		"\2\u2665\2\u2667\2\u2668\2\u266a\2\u266a\2\u267d\2\u267d\2\u2681\2\u2681"+
		"\2\u2694\2\u2699\2\u269b\2\u269b\2\u269d\2\u269e\2\u26a2\2\u26a3\2\u26ac"+
		"\2\u26ad\2\u26b2\2\u26b3\2\u26bf\2\u26c0\2\u26c6\2\u26c7\2\u26ca\2\u26ca"+
		"\2\u26d0\2\u26d1\2\u26d3\2\u26d3\2\u26d5\2\u26d6\2\u26eb\2\u26ec\2\u26f2"+
		"\2\u26f7\2\u26f9\2\u26fc\2\u26ff\2\u26ff\2\u2704\2\u2704\2\u2707\2\u2707"+
		"\2\u270a\2\u270f\2\u2711\2\u2711\2\u2714\2\u2714\2\u2716\2\u2716\2\u2718"+
		"\2\u2718\2\u271f\2\u271f\2\u2723\2\u2723\2\u272a\2\u272a\2\u2735\2\u2736"+
		"\2\u2746\2\u2746\2\u2749\2\u2749\2\u274e\2\u274e\2\u2750\2\u2750\2\u2755"+
		"\2\u2757\2\u2759\2\u2759\2\u2765\2\u2766\2\u2797\2\u2799\2\u27a3\2\u27a3"+
		"\2\u27b2\2\u27b2\2\u27c1\2\u27c1\2\u2936\2\u2937\2\u2b07\2\u2b09\2\u2b1d"+
		"\2\u2b1e\2\u2b52\2\u2b52\2\u2b57\2\u2b57\2\u3032\2\u3032\2\u303f\2\u303f"+
		"\2\u3299\2\u3299\2\u329b\2\u329b\2\uf006\3\uf006\3\uf0d1\3\uf0d1\3\uf172"+
		"\3\uf173\3\uf180\3\uf181\3\uf190\3\uf190\3\uf193\3\uf19c\3\uf1e8\3\uf201"+
		"\3\uf203\3\uf204\3\uf21c\3\uf21c\3\uf231\3\uf231\3\uf234\3\uf23c\3\uf252"+
		"\3\uf253\3\uf302\3\uf323\3\uf326\3\uf395\3\uf398\3\uf399\3\uf39b\3\uf39d"+
		"\3\uf3a0\3\uf3f2\3\uf3f5\3\uf3f7\3\uf3f9\3\uf4ff\3\uf501\3\uf53f\3\uf54b"+
		"\3\uf550\3\uf552\3\uf569\3\uf571\3\uf572\3\uf575\3\uf57c\3\uf589\3\uf589"+
		"\3\uf58c\3\uf58f\3\uf592\3\uf592\3\uf597\3\uf598\3\uf5a6\3\uf5a7\3\uf5aa"+
		"\3\uf5aa\3\uf5b3\3\uf5b4\3\uf5be\3\uf5be\3\uf5c4\3\uf5c6\3\uf5d3\3\uf5d5"+
		"\3\uf5de\3\uf5e0\3\uf5e3\3\uf5e3\3\uf5e5\3\uf5e5\3\uf5ea\3\uf5ea\3\uf5f1"+
		"\3\uf5f1\3\uf5f5\3\uf5f5\3\uf5fc\3\uf651\3\uf682\3\uf6c7\3\uf6cd\3\uf6d4"+
		"\3\uf6e2\3\uf6e7\3\uf6eb\3\uf6eb\3\uf6ed\3\uf6ee\3\uf6f2\3\uf6f2\3\uf6f5"+
		"\3\uf6fa\3\uf912\3\uf93c\3\uf93e\3\uf940\3\uf942\3\uf947\3\uf949\3\uf94e"+
		"\3\uf952\3\uf96d\3\uf982\3\uf999\3\uf9c2\3\uf9c2\3\uf9d2\3\uf9e8\3\16"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\3\t\3\2\2\2\5\13\3\2\2\2\7\r\3\2"+
		"\2\2\t\n\7\"\2\2\n\4\3\2\2\2\13\f\7\f\2\2\f\6\3\2\2\2\r\16\t\2\2\2\16"+
		"\b\3\2\2\2\3\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}