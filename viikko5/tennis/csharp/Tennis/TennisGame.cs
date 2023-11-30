namespace Tennis
{
      public class TennisGame
      {
            protected string player1Name;
            protected string player2Name;
            protected int p1Score;
            protected int p2Score;

            public TennisGame(string player1Name, string player2Name)
            {
                  this.player1Name = player1Name;
                  this.player2Name = player2Name;
            }

            public void WonPoint(string playerName)
            {
                  if (player1Name.Equals(playerName)) p1Score++;
                  else if (player2Name.Equals(playerName)) p2Score++;
            }

            public string GetScore()
            {
                  if (p1Score == p2Score)
                  {
                        return GetTieResult(p1Score);
                  }
                  else if (p1Score >= 4 || p2Score >= 4)
                  {
                        return GetEndGameResult(p1Score, p2Score);
                  }
                  string p1RegularScore = GetRegularScoreString(p1Score);
                  string p2RegularScore = GetRegularScoreString(p2Score);
                  return $"{p1RegularScore}-{p2RegularScore}";
            }

            private static string GetRegularScoreString(int score)
            {
                  return score switch
                  {
                        0 => "Love",
                        1 => "Fifteen",
                        2 => "Thirty",
                        _ => "Forty",
                  };
            }

            private string GetEndGameResult(int score1, int score2)
            {
                  return (score1 - score2) switch
                  {
                        1 => $"Advantage {player1Name}",
                        -1 => $"Advantage {player2Name}",
                        >= 2 => $"Win for {player1Name}",
                        _ => $"Win for {player2Name}",
                  };
            }

            private static string GetTieResult(int score)
            {
                  return score switch
                  {
                        0 => "Love-All",
                        1 => "Fifteen-All",
                        2 => "Thirty-All",
                        _ => "Deuce",
                  };
            }
      }
}

