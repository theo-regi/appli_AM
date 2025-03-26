"""By Régi Théo"""
from database.models import PortfolioDB, PositionDB
from scripts.assets import Shares
from scripts.registry import LIST_SOURCES, LIST_TYPES
#_______________________________________________________________________________________________________
#----------------------------Scripts to implement utils classes ----------------------------------------
#_______________________________________________________________________________________________________

#-------------------------------------------------------------------------------------------------------
#----------------------------Classes for DB Interractions------ ----------------------------------------
#-------------------------------------------------------------------------------------------------------
#Class to store the portfolios in the database
class PortfolioStore:
    """
    Class to store the portfolios in the database

    Input:
    - session: sqlalchemy.orm.session.Session: session to interact with the database
    """
    def __init__(self, session):
        self.session = session

    def save_portfolio(self, portfolio):
        self.delete_portfolio(portfolio.name)

        ptf_db = PortfolioDB(
            name=portfolio.name,
            invested_capital=portfolio.invested_capital
        )
        self.session.add(ptf_db)
        self.session.commit()

        for pos in portfolio.all_positions:
            pos_db = PositionDB(
                portfolio_id=ptf_db.id,
                isin=pos.isin,
                pru=pos.pru,
                quantity=pos.quantity,
                date_achat=pos.date_achat,
                type=pos.type,
                source=pos.source.__class__.__name__
            )
            self.session.add(pos_db)

        self.session.commit()

    def load_portfolios(self) -> dict:
        from scripts.portfolio import Portfolio
        portfolios = {}
        ptf_rows = self.session.query(PortfolioDB).all()
        for ptf_row in ptf_rows:
            ptf = Portfolio(name=ptf_row.name, invested_capital=ptf_row.invested_capital)

            # Load associated positions
            positions = self.session.query(PositionDB).filter_by(portfolio_id=ptf_row.id).all()
            for pos_row in positions:
                # Create the correct asset type (here only 'Shares')
                if pos_row.type == "Shares":
                    pos = Shares(
                        isin=pos_row.isin,
                        source=LIST_SOURCES[pos_row.source](),
                        pru=pos_row.pru,
                        quantity=pos_row.quantity,
                        date_achat=pos_row.date_achat
                    )
                    ptf.buy_position(pos_row.isin, pos)
                else:
                    print(f"⚠️ Unsupported type '{pos_row.type}' found in DB.")

            portfolios[ptf_row.name] = ptf
        return portfolios

    def delete_portfolio(self, name):
        ptf = self.session.query(PortfolioDB).filter_by(name=name).first()
        if ptf is not None:
            self.session.delete(ptf)
            self.session.commit()
            return True
        return False