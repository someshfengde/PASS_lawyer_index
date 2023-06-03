import {
	loadQAMapReduceChain,
	loadQAStuffChain,
	loadQARefineChain,
	RefineDocumentsChain,
} from 'langchain/chains'
import { TokenTextSplitter } from 'langchain/text_splitter'
import { HNSWLib } from 'langchain/vectorstores/hnswlib'
import * as dotenv from 'dotenv'
import { OpenAI } from 'langchain/llms/openai'
import { Document } from 'langchain/document'
import { OpenAIEmbeddings } from 'langchain/embeddings/openai'
import { TextLoader } from 'langchain/document_loaders/fs/text'
import { DirectoryLoader } from 'langchain/document_loaders/fs/directory'
import { PromptTemplate } from 'langchain/prompts'
import { StructuredOutputParser } from 'langchain/output_parsers'

import express from 'express'

const app = express()

dotenv.config()

// const a1_loader = new DirectoryLoader('../dataset/summary/A1', {
// 	'.txt': (path) => new TextLoader(path),
// })
// const a2_loader = new DirectoryLoader('../dataset/summary/A2', {
// 	'.txt': (path) => new TextLoader(path),
// })
// const judgement_loader = new DirectoryLoader('../dataset/judgement', {
// 	'.txt': (path) => new TextLoader(path),
// })
// const main_documents = new DirectoryLoader('../converted_text', {
// 	'.txt': (path) => new TextLoader(path),
// })
// const main_documents_new = new DirectoryLoader('../conv_text_new', {
// 	'.txt': (path) => new TextLoader(path),
// })

// let docs = []

// // docs.push(await a1_loader.load())
// // docs.push(await a2_loader.load())
// // docs.push(await judgement_loader.load())
// docs.push(await main_documents_new.load())

// docs = docs.flat()

// const splitter = new TokenTextSplitter({
// 	chunkSize: 400,
// 	chunkOverlap: 20,
// 	encodingName: 'cl100k_base',
// })

// const data = []

// for await (const doc of docs) {
// 	const chunks = await splitter.splitDocuments([doc])

// 	const params = doc.metadata.source.match(
// 		/conv_text_new\/([^\/]+)_on_(.+)\.txt$/
// 	)

// 	let case_name = params[1],
// 		case_date = params[2]

// 	chunks.forEach((chunk, i) => {
// 		data.push(
// 			new Document({
// 				pageContent: chunk.pageContent,
// 				metadata: {
// 					id: `${case_name}-${i}`,
// 					case_name,
// 					case_date,
// 				},
// 			})
// 		)
// 	})
// }

// const vectorStore = await HNSWLib.fromDocuments(
// 	data,
// 	new OpenAIEmbeddings({
// 		openAIApiKey: process.env.OPENAI,
// 		verbose: true,
// 	})
// )

// await vectorStore.save('../hnswlib_new')
// await vectorStore.save('../hnswlib')

// const vectorStore = await HNSWLib.load(
// 	'../hnswlib',
// 	new OpenAIEmbeddings({
// 		openAIApiKey: process.env.OPENAI,
// 		verbose: true,
// 	})
// )
const vectorStore = await HNSWLib.load(
	'../hnswlib_new',
	new OpenAIEmbeddings({
		openAIApiKey: process.env.OPENAI,
		verbose: true,
	})
)

const model = new OpenAI({
	modelName: 'gpt-3.5-turbo',
	openAIApiKey: process.env.OPENAI,
	verbose: true,
})

const chain = loadQAMapReduceChain(model, {
	verbose: true,
	returnSourceDocuments: true,
})

app.get('/hello', (req, res) => {
	res.send({ hello: 'world' })
})

app.get('/query', async (req, res) => {
	try {
		const query = req.query.search

		const docs = await vectorStore.similaritySearch(query)

		const response = []

		for await (const doc of docs) {
			let argument_res,
				interpretation_res,
				articles_res,
				background_res,
				clause_res,
				points_res,
				submission_res

			const caseArray = []

			caseArray.push(
				new Promise(async (resolve) => {
					const argumentDocs = await vectorStore.similaritySearch(
						'argument made by the respondent',
						2,
						(document) =>
							document.metadata.case_name ===
							doc.metadata.case_name
					)
					argument_res = await chain.call({
						input_documents: argumentDocs,
						question: 'summarize the docs',
					})

					resolve()
				})
			)
			caseArray.push(
				new Promise(async (resolve) => {
					const interpretationDocs =
						await vectorStore.similaritySearch(
							'what is the interpretation of the case',
							2,
							(document) =>
								document.metadata.case_name ===
								doc.metadata.case_name
						)
					interpretation_res = await chain.call({
						input_documents: interpretationDocs,
						question: 'summarize the docs',
					})

					resolve()
				})
			)
			caseArray.push(
				new Promise(async (resolve) => {
					const articlesDocs = await vectorStore.similaritySearch(
						'what are the articles used and their description',
						2,
						(document) =>
							document.metadata.case_name ===
							doc.metadata.case_name
					)
					articles_res = await chain.call({
						input_documents: articlesDocs,
						question: 'summarize the docs',
					})

					resolve()
				})
			)
			caseArray.push(
				new Promise(async (resolve) => {
					const backgroundDocs = await vectorStore.similaritySearch(
						'what is the background of the case',
						2,
						(document) =>
							document.metadata.case_name ===
							doc.metadata.case_name
					)
					background_res = await chain.call({
						input_documents: backgroundDocs,
						question: 'summarize the docs',
					})

					resolve()
				})
			)
			caseArray.push(
				new Promise(async (resolve) => {
					const clausesDocs = await vectorStore.similaritySearch(
						'what are the clauses of the case',
						2,
						(document) =>
							document.metadata.case_name ===
							doc.metadata.case_name
					)
					clause_res = await chain.call({
						input_documents: clausesDocs,
						question: 'summarize the docs',
					})

					resolve()
				})
			)
			caseArray.push(
				new Promise(async (resolve) => {
					const pointsDocs = await vectorStore.similaritySearch(
						'what are the proven points in case',
						2,
						(document) =>
							document.metadata.case_name ===
							doc.metadata.case_name
					)
					points_res = await chain.call({
						input_documents: pointsDocs,
						question: 'summarize the docs',
					})

					resolve()
				})
			)
			caseArray.push(
				new Promise(async (resolve) => {
					const submissionDocs = await vectorStore.similaritySearch(
						'what are the submissions in the case',
						2,
						(document) =>
							document.metadata.case_name ===
							doc.metadata.case_name
					)
					submission_res = await chain.call({
						input_documents: submissionDocs,
						question: 'summarize the docs',
					})

					resolve()
				})
			)

			await Promise.all(caseArray)

			response.push({
				argument_res,
				interpretation_res,
				articles_res,
				background_res,
				clause_res,
				points_res,
				submission_res,
				case: {
					date: doc.metadata.case_date,
					name: doc.metadata.case_name,
				},
			})
		}

		res.send({ docs, response })
	} catch (error) {
		res.send(error)
	}
})

app.listen(3000, '0.0.0.0', () => console.log('server connected!'))
