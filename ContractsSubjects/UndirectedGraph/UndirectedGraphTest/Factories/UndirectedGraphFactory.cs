// <copyright file="UndirectedGraphFactory001.cs">Copyright ? 2018</copyright>

using System;
using Microsoft.Pex.Framework;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using UndirectedGraph;
using Common.Utility;
using PexAPIWrapper;

namespace UndirectedGraph.Test.Factories
{
    /// <summary>A factory for QuickGraph.UndirectedGraph`2[System.String,QuickGraph.Edge`1[System.String]] instances</summary>
    public static partial class UndirectedGraphFactory
    {
        /*1. Add one Vertex*/
        [PexFactoryMethod(typeof(UndirectedGraph.UndirectedGraph<int, Edge<int>>))]
        public static UndirectedGraph<int, Edge<int>> CreateGraphOneNode(int node1)
        {
            UndirectedGraph<int, Edge<int>> g = new UndirectedGraph<int, Edge<int>>(false);
            g.AddVertex(node1);
            return g;

        }

        /*2. Add array of vertex (no edges) - check distinct elements and not zero */
        /*[PexFactoryMethod(typeof(QuickGraph.UndirectedGraph<int, Edge<int>>))]
        public static UndirectedGraph<int, Edge<int>> CreateGraphArrayOfNodes([PexAssumeNotNull]int[] nodes)
        {
            //PexAssume.IsTrue(nodes.Length < 12);
            PexAssume.AreDistinctValues(nodes);
            PexAssume.TrueForAll(nodes, e => e != 0);
            UndirectedGraph<int, Edge<int>> g = new UndirectedGraph<int, Edge<int>>(false);
            foreach (int ele in nodes)
                g.AddVertex(ele);
            return g;
        }*/

        [PexFactoryMethod(typeof(UndirectedGraph.UndirectedGraph<int, Edge<int>>))]
        public static UndirectedGraph<int, Edge<int>> CreateGraphArrayOfNodesAndEdges([PexAssumeNotNull]int[] nodes,
            [PexAssumeNotNull] bool[] edges)
        {
            PexAssume.IsTrue(edges.Length <= nodes.Length);
            PexAssume.AreDistinctValues(nodes);
            PexAssume.TrueForAll(nodes, e => e != 0);

            UndirectedGraph<int, Edge<int>> g = new UndirectedGraph<int, Edge<int>>(false);
            foreach (int ele in nodes)
            {
                g.AddVertex(ele);
            }

            for (int i = 0; i < edges.Length; i++)
            {
                int source = PexChoose.IndexValue("indexed value", nodes);
                if (edges[i] == false)
                    g.AddEdge(new Edge<int>(nodes[source], nodes[i]));
            }
            return g;
        }

        [PexFactoryMethod(typeof(UndirectedGraph.UndirectedGraph<int, Edge<int>>))]
        public static UndirectedGraph<int, Edge<int>> CreateGraphArrayOfNodesAndEdgesAssume([PexAssumeNotNull]int[] nodes,
            [PexAssumeNotNull] bool[] edges)
        {
            //PexAssume.IsTrue(nodes.Length <= 7 || nodes.Length > 7);
            PexAssume.IsTrue(edges.Length <= 6 || nodes.Length > 6);
            PexAssume.IsTrue(edges.Length <= nodes.Length);
            PexAssume.AreDistinctValues(nodes);
            //PexAssume.TrueForAll(nodes, e => e != 0);

            UndirectedGraph<int, Edge<int>> g = new UndirectedGraph<int, Edge<int>>(false);
            foreach (int ele in nodes)
            {
                g.AddVertex(ele);
            }

            int source = PexChoose.IndexValue("indexed value", nodes);

            for (int i = 0; i < edges.Length; i++)
            {

                if (edges[i] == false)
                    g.AddEdge(new Edge<int>(nodes[source], nodes[i]));
            }
            return g;
        }

        //[PexFactoryMethod(typeof(UndirectedGraph.UndirectedGraph<int, Edge<int>>))]
        //public static UndirectedGraph<int, Edge<int>> CreateGraphByNumNodesConstantEdges(int num)
        //{
        //    bool allowParallelEdges = PexChoose.Value<bool>("allowParallelEdges");
        //    UndirectedGraph<int, Edge<int>> g = new UndirectedGraph<int, Edge<int>>(allowParallelEdges);

        //    //UndirectedGraph<int, Edge<int>> g = new UndirectedGraph<int, Edge<int>>(false);
        //    PexAssume.IsTrue(num > 0 && num < 11);


        //    for (int i = 0; i < num; i++)
        //    {
        //        g.AddVertex(i);
        //    }

        //    for (int i = 1; i < num; i++)
        //    {
        //        g.AddEdge(new Edge<int>(0, i));
        //    }

        //    return g;
        //}

        //[PexFactoryMethod(typeof(UndirectedGraph.UndirectedGraph<int, Edge<int>>))]
        //public static UndirectedGraph<int, Edge<int>> CreateGraphByNumNodesPexChooseEdges(int num)
        //{
        //    bool allowParallelEdges = PexChoose.Value<bool>("allowParallelEdges");
        //    UndirectedGraph<int, Edge<int>> g = new UndirectedGraph<int, Edge<int>>(!allowParallelEdges);

        //    //UndirectedGraph<int, Edge<int>> g = new UndirectedGraph<int, Edge<int>>(false);
        //    PexAssume.IsTrue(num > 0 && num < 20);


        //    for (int i = 0; i < num; i++)
        //    {
        //        g.AddVertex(i);
        //    }

        //    for (int i = 0; i < num; i++)
        //    {
        //        for (int j = i + 1; j < num; j++)
        //        {
        //            bool add = PexChoose.Value<bool>("add");
        //            if (!add)
        //            {
        //                g.AddEdge(new Edge<int>(i, j));
        //            }
        //        }
        //    }

        //    return g;
        //}

        //[PexFactoryMethod(typeof(UndirectedGraph.UndirectedGraph<int, Edge<int>>))]
        //public static UndirectedGraph<int, Edge<int>> CreateGraphByNumNodesNumEdgesPexChoose(int numVertex, int numEdge)
        //{
        //    bool allowParallelEdges = PexChoose.Value<bool>("allowParallelEdges");
        //    UndirectedGraph<int, Edge<int>> g = new UndirectedGraph<int, Edge<int>>(allowParallelEdges);

        //    //UndirectedGraph<int, Edge<int>> g = new UndirectedGraph<int, Edge<int>>(false);
        //    PexAssume.IsTrue(numVertex > 0 && numVertex < 20);
        //    PexAssume.IsTrue(numEdge > 0 && numEdge < 20);


        //    for (int i = 0; i < numVertex; i++)
        //    {
        //        int value = PexChoose.Value<int>("value");
        //        if (!g.ContainsVertex(value))
        //        {
        //            g.AddVertex(i);
        //        }
        //    }

        //    for (int i = 0; i < numEdge; i++)
        //    {
        //        int source = PexChoose.Value<int>("value");
        //        int target = PexChoose.Value<int>("target");
        //        if (!g.ContainsVertex(source))
        //        {
        //            g.AddVertex(source);
        //        }

        //        if (!g.ContainsVertex(target))
        //        {
        //            g.AddVertex(target);
        //        }

        //        if (source != target)
        //        {
        //            g.AddEdge(new Edge<int>(source, target));
        //        }
        //    }


        //    return g;

        //}

    }
}
