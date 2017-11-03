#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author  : Geoffrey

import re
import timeit


class Prule(object):

    """docstring for rule"""

    def __init__(self, name, rule):
        self.name = name
        self.rule = rule


class AgendaManager(object):

    """docstring for AgendaManager"""

    def __init__(self):
        print ('\t\t--AgendaManager--\n')
        #self.Performing='performing'
        self.rulelist = list()
        self.cycle=0

    def get_rules(self):
        try:
            filename=str(input("Enter the filename : "))
            files = open(filename, 'r')
            for line in files:
            	if(len(line.strip())==0):
            		continue
            	else:
            		rule = re.findall(r'\(.*?\)', line)
            		for rules in rule:
            			temp = rules.split(',')
            			temp1 = temp[0].split('(')
            			temp2 = temp[1].split(')')
            			temp2=int(temp2[0])
            			rule1= Prule(temp1[1], temp2)
            			self.rulelist.append(rule1)
            		AM.BuildQ()
            		AM.Delete()
            	
        except:
            filename=str(input("Enter the filename : "))
            files = open(filename, 'r')
            for line in files:
            	rule = re.findall(r'\(.*?\)', line)
            	for rules in rule:
            		temp = rules.split(',')
            		temp1 = temp[0].split('(')
            		temp2 = temp[1].split(')')
            		temp2=int(temp2[0])
            		rule1= Prule(temp1[1], temp2)
            		self.rulelist.append(rule1)
            	AM.BuildQ()
            	AM.Delete()

    def Insert(self,element):
        self.rulelist.append((element))
        
    def ExtractMax(self):
        Max = self.rulelist.pop(0)
        self.cycle += 1
        print("Cycle {} Completed ----------->\n Rule {} with Priority {} has been Executed  \n ".format(self.cycle,Max.name,Max.rule,))

        n=len(self.rulelist)
        for i in reversed(range(n // 2)):
            self.rulelist[i],self.rulelist[1]=self.rulelist[i],self.rulelist[1]
            AM.hepify(n,i)

    def Delete(self):
        #poping out the first prioritised element from the list
        if(self.cycle<=30):
        	Max = self.rulelist.pop(0)
        	print("Cycle {} Completed -----------> \n Rule {} with Priority {} has been Executed  \n ".format(self.cycle,Max.name,Max.rule,))
        	self.cycle += 1
        else:
        	print("{} Cycle's completed ".format(self.cycle-1))

        

    def printrules(self):
        print ('\tprinting the rules from the rule list')
        count = 1
        for rule in self.rulelist:
            print ('Rule {} is {},Priority{}'.format(count, rule.name,
                    rule.rule))
            count += 1  


    def hepify(self,n,i):
        #print ('{} hepify at {}'.format(self.Performing,i))
        largest=i
        l=2*i+1
        r=2*i+2
        
        if(l<n and self.rulelist[l].rule>self.rulelist[i].rule):
            largest=l
        else:
            largest=i
        if(r<n and self.rulelist[r].rule>self.rulelist[largest].rule):
            largest=r
        if(largest!=i):
            self.rulelist[i],self.rulelist[largest]=self.rulelist[largest],self.rulelist[i]
            AM.hepify(n,largest)

    def BuildQ(self):
        #print ('\tBuilding the queue')
        n = len(self.rulelist)
        #print ('The length of the Array is {}'.format(n))
        for i in reversed(range(n // 2)):
            self.rulelist[i],self.rulelist[1]=self.rulelist[i],self.rulelist[1]
            AM.hepify(n,i)
            


if __name__ == '__main__':
    AM = AgendaManager()
    start = timeit.default_timer()
    rulelist = AM.get_rules()
    while(AM.cycle < 30 and len(AM.rulelist)>0):
    	AM.ExtractMax()
    stop = timeit.default_timer()
    print("\n \tThe execution time of the program is {}".format(stop-start))
    
    

