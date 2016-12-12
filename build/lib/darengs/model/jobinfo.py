"""job model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relation, backref

from darengs.model.meta import Base


class jobinfo(Base):
    __tablename__ = "jobinfo"
    #__mapper_args__ = dict(order_by="submitted_time desc")

    id             = Column(Integer, primary_key = True)
    description    = Column(String(200), default = "")
    submitted_time = Column( String(100), default = "")
    key            = Column(String(50), default = "") 
    value          = Column(String(50), default = "") 
    jobid          = Column( Integer, ForeignKey('job.id') )
    
    #assign relation to access the realtion backre job.jobinfo or jobinfo.jobs
    jobs = relation('job', backref=backref('jobinfo'))

    
    
    def __init__(self):
        #self.appname = appname
        #self.email = email
        pass
        
# def __repr__(self):
# pass
  #return '%s')" % self.appname       
#addresses = relationship("Address",
		 #       primaryjoin="and_(User.id==Address.user_id, "
	   #             "Address.email.startswith('tony'))",
		#        backref="user") 
#cascade="all,delete-orphan"
                    #job disc
                    #job_location: local or remote