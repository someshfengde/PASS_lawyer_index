import {
	loadQAMapReduceChain,
	loadQAStuffChain,
	loadQARefineChain,
} from 'langchain/chains'
import { TokenTextSplitter } from 'langchain/text_splitter'
import { HNSWLib } from 'langchain/vectorstores/hnswlib'
import * as dotenv from 'dotenv'
import { OpenAI } from 'langchain/llms/openai'
import { Document } from 'langchain/document'
import { OpenAIEmbeddings } from 'langchain/embeddings/openai'
import { TextLoader } from 'langchain/document_loaders/fs/text'
import { DirectoryLoader } from 'langchain/document_loaders/fs/directory'

import express from 'express'

const app = express()

dotenv.config()

const a1_loader = new DirectoryLoader('../dataset/summary/A1', {
	'.txt': (path) => new TextLoader(path),
})
const a2_loader = new DirectoryLoader('../dataset/summary/A2', {
	'.txt': (path) => new TextLoader(path),
})
const judgement_loader = new DirectoryLoader('../dataset/judgement', {
	'.txt': (path) => new TextLoader(path),
})
const main_documents = new DirectoryLoader('../converted_text', {
	'.txt': (path) => new TextLoader(path),
})

let docs = []

// docs.push(await a1_loader.load())
// docs.push(await a2_loader.load())
// docs.push(await judgement_loader.load())
docs.push(await main_documents.load())

docs = docs.flat()

const splitter = new TokenTextSplitter({
	chunkSize: 400,
	chunkOverlap: 20,
	encodingName: 'cl100k_base',
})

const data = []

console.log(docs);

// for await (const doc of docs) {
// 	const chunks = await splitter.splitDocuments([doc])

// 	const params = doc.metadata.source.match(
// 		/\/([^\/]+)\/([^\/]+)\/([^\/]+)\.txt$/
// 	)

// 	let type, author, case_date

// 	if (params.includes('summary')) {
// 		type = params[1]
// 		author = params[2]
// 		case_date = params[3]
// 	} else if (params.includes('judgement')) {
// 		type = params[2]
// 		case_date = params[3]
// 	}
// 	chunks.forEach((chunk, i) =>
// 		data.push(
// 			new Document({
// 				pageContent: chunk.pageContent,
// 				metadata: {
// 					id: `${case_date}-${i}`,
// 					type,
// 					case_date,
// 					author,
// 				},
// 			})
// 		)
// 	)
// }

// const vectorStore = await HNSWLib.fromDocuments(
// 	data,
// 	new OpenAIEmbeddings({
// 		openAIApiKey: process.env.OPENAI,
// 		verbose: true,
// 	})
// )

// const model = new OpenAI({
// 	modelName: 'gpt-3.5-turbo',
// 	openAIApiKey: process.env.OPENAI,
// 	verbose: true,
// })

// const chain = loadQAStuffChain(model, {
// 	verbose: true,
// 	returnSourceDocuments: true,
// })

// app.get('/hello', (req, res) => {
// 	res.send({ hello: 'world' })
// })

// app.get('/query', async (req, res) => {
// 	try {
// 		const query = req.query.search

// 		const docs = await vectorStore.similaritySearch(query)

// 		const response = await chain.call({
// 			input_documents: docs,
// 			question: 'summarize the above documents',
// 		})

// 		res.send({ docs, response })
// 	} catch (error) {
// 		res.send(error)
// 	}
// })

// app.listen(3000, '0.0.0.0', () => console.log('server connected!'))
