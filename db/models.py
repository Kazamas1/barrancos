from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Staging_Barrancos(Base):
    __tablename__ = 'Staging_Barrancos'
    Zona  = Column(String)
    Cod_zona  = Column(String)
    N_libro = Column(Integer, primary_key=True)
    Recorrido_Total = Column(Integer)
    Recorrido_torrente = Column(Integer)
    Desnivel_Total = Column(Integer)
    Rapel_maximo = Column(Integer)
    m100 = Column(Integer)
    m90m = Column(Integer)
    m80 = Column(Integer)
    m70m = Column(Integer)
    m60 = Column(Integer)
    m50 = Column(Integer)
    m45 = Column(Integer)
    m40 = Column(Integer)
    m30 = Column(Integer)
    m25 = Column(Integer)
    m20 = Column(Integer)
    m15 = Column(Integer)
    m10 = Column(Integer)
    t_acceso  = Column(String)
    t_torrente  = Column(String)
    t_retorno  = Column(String)
    dificultad  = Column(String)
    carga  = Column(String)
    Ini_carrega = Column(Integer)
    full_carrega = Column(Integer)
    Hidrologia  = Column(String)
    
    def __repr__(self):
        return "<Staging_Barrancos(Zona='{}',Cod_zona='{}',N_libro='{}',Recorrido_Total='{}',Recorrido_torrente='{}',Desnivel_Total='{}',Rapel_maximo='{}',m100='{}',m90m='{}',m80='{}',m70m='{}',m60='{}',m50='{}',m45='{}',m40='{}',m30='{}',m25='{}',m20='{}',m15='{}',m10='{}',t_acceso='{}',t_torrente='{}',t_retorno='{}',dificultad='{}',carga='{}',Ini_carrega='{}',full_carrega='{}',Hidrologia='{}')>"\
                .format(self.Zona ,self.Cod_zona ,self.N_libro ,self.Recorrido_Total ,self.Recorrido_torrente ,self.Desnivel_Total ,self.Rapel_maximo ,self.m100 ,self.m90m ,self.m80 ,self.m70m ,self.m60 ,self.m50 ,self.m45 ,self.m40 ,self.m30 ,self.m25 ,self.m20 ,self.m15 ,self.m10 ,self.t_acceso ,self.t_torrente ,self.t_retorno ,self.dificultad ,self.carga ,self.Ini_carrega ,self.full_carrega ,self.Hidrologia)
                



