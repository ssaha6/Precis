from z3 import *
import itertools
from Data.precis_feature import PrecisFeature
from Data.feature_vector import FeatureVector

class Houdini:
    
    useBounds = False

    def concatenateFeatureVectors(self, baseFeatureVectors, derivedValuesZ3Tuples):
        featureVectors = []
        for i in range(len(baseFeatureVectors)):
            featureVectors.append(baseFeatureVectors[i] + derivedValuesZ3Tuples[i])
        return featureVectors
    
    def getBoolFeatures(self, precisFeatureList):
        boolFeatures = []
        boolFeatureIndices = []
        for idx in range(len(precisFeatureList)):
            if is_bool(precisFeatureList[idx].varZ3):
                boolFeatures.append(precisFeatureList[idx])
                boolFeatureIndices.append(idx)
        return boolFeatures, boolFeatureIndices
    
    def getBoolFeatureVectors(self, featureVectorList):
        assert(len(featureVectorList) > 0)
        boolFeatureVectorIndices = self.getBoolFeatureVector(featureVectorList[0])
        boolFeatureVectors = []
        for featureVector in featureVectorList:
            boolFeatureVector = FeatureVector([], [], str(featureVector.testLabel))
            boolFeatureVector.valuesZ3 = tuple(featureVector.valuesZ3[i] for i in boolFeatureVectorIndices)
            boolFeatureVector.values = tuple(featureVector.values[i] for i in boolFeatureVectorIndices)
            boolFeatureVectors.append(boolFeatureVector)
        return boolFeatureVectors, boolFeatureVectorIndices

    def getBoolFeatureVector(self, featureVector):
        boolFeatureVectorIndices = []
        for idx in range(len(featureVector.valuesZ3)):
            if is_bool(featureVector.valuesZ3[idx]):
                boolFeatureVectorIndices.append(idx)
        return boolFeatureVectorIndices

    def generateDerivedFeatureVectors(self, derivedFeatures, baseFeatures, baseFeatureVectors):
        
        print(derivedFeatures)
        print(baseFeatureVectors)
        print ("here")
        print(baseFeatures)
        pairs = list()
        # consider
        allDerivedFeatureVectors = list()
        for f in baseFeatureVectors:
            print("feature vec: " +str(f))
            pairs = Houdini.generateFeatureValueMapping(baseFeatures,f)
            print(pairs)
            #print(type(pairs))
            derivedFeatureVector = ()
            for df in derivedFeatures:
                deriveFeatVec = substitute(df.varZ3 , pairs)
                deriveFeatVecValue = simplify(deriveFeatVec)
                derivedFeatureVector += (deriveFeatVecValue,)
            # Assert: # of derived feature values(i.e. length of derived feature vector(tuple)) should be the same as
            # Assert: # of derived features (.i.e length of list of derived features)
            assert(len(derivedFeatureVector) == len(derivedFeatures))
            
            allDerivedFeatureVectors.append(derivedFeatureVector)
        
        #print(allDerivedFeatureVectors)
        return allDerivedFeatureVectors

    @staticmethod
    def generateFeatureValueMapping(baseFeatures, featureVector):
        pairs = list()
        # consider removing check for perfomances in cases where the number of feature vectors gets large.
        # number of base features should be the same as the number of entries in feature vector(values of said features)
        assert(len(featureVector) == len(baseFeatures))
        for i in  range(len(baseFeatures)):
            #print("type of featVec", type(featureVector[i]))
            pair = (baseFeatures[i].varZ3 , featureVector[i])
            pairs.append(pair)
        return pairs


    def learn(features,featureVectors):
        assert(len(featureVectors) > 0)
        #check datapoint are boolean
        #assert(len(self.dataPoints) or all ( all( v == "true" or v == "false" for v in dp) for dp in self.dataPoints))
    
    """
     def runLearner(self):
        #print os.linesep+ " bool variables renamed again: " + str(self.symbolicBoolVariables)
        # Numpy implementation, future work
        # A = np.array(np.array(self.dataPoints) == "true")
        # X, y = A[:, :-1], A[:, -1]
        assert(len(self.dataPoints)> 0 )
        #asset all data point elements are "true" or "false"
        #if len(self.dataPoints) == 0:
        #    self.learntConjuction = ["true"]
        #    return "true"

        assert(len(self.dataPoints) or all ( all( v == "true" or v == "false" for v in dp) for dp in self.dataPoints))
        
        #Assign all predicate to true
        predAssignment = {varIndex: True for varIndex in range(0, len(self.symbolicBoolVariables))} 
        
        for varIndex in range(0, len(self.symbolicBoolVariables)):
            # not needed, but useful to prune: If a predicate is already evaluated to Flase, skip 
            if predAssignment[varIndex] == False:
                continue
            
            for dp in self.dataPoints:
                #There are no negative points for postcondition learning!!! Should not check for this
                if dp[-1] == "false":
                    #continue 
                    raise ValueError("Inspect ME, I may be wrong")
                
                #datapoint is posetive 
                #if datapoint on predicate is false
                if dp[varIndex]  == "false":
                    predAssignment[varIndex]  = False
                    break
        
        posPred = []
        for varIndex in range(0, len(self.symbolicBoolVariables)):
            if predAssignment[varIndex]:
                posPred.append(self.symbolicBoolVariables[varIndex])
        


        # This is also wrong!, if no positive predicates than we should not output false but rather TRUE;
        if len(posPred) == 0:
            conjunct = "true"
            # Quick Fix- to return list
            self.learntConjuction = ["true"]
        
        elif len(posPred) == 1:
            conjunct = posPred[0]
            # Quick Fix- to return list
            self.learntConjuction = posPred
        else: 
            conjunct = "(and " + " ".join(posPred) + ")"
            self.learntConjuction = posPred
        #print os.linesep+ "conjunct from houdini: "+ conjunct
        return conjunct
    """